from django import template
from django.db.models import Q
from menu.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_main_menu(context, menu_name):
    """
        Отображает меню на веб-странице.

        Аргументы:
            context: объект context, содержащий информацию о текущем запросе
            menu_name: имя меню, которое нужно отобразить на странице

        Возвращает:
            Словарь с элементом menu, содержащим список элементов меню и их дочерних элементов.

        Каждый элемент меню может содержать следующие поля:
            id: уникальный идентификатор элемента
            name: имя элемента
            url: адрес страницы, на которую ведет элемент меню
            named_url: имя именованного адреса, на которую ведет элемент меню
            parent: родительский элемент меню (None, если элемент верхнего уровня)
            children: список дочерних элементов меню
            is_active: флаг, указывающий, является ли элемент активным на текущей странице
        """

    menu = Menu.objects.filter(Q(name=menu_name) | Q(parent__name=menu_name)).order_by('parent__id', 'id')

    def make_tree(menu_tree, parent=None):
        tree = []
        for items in menu:
            if item.parent == parent:
                children = make_tree(menu_tree, items)
                if children:
                    item.children = children
                tree.append(item)
        return tree

    menu = make_tree(menu)

    request = context['request']
    for item in menu:
        if item.url:
            item.is_active = request.path == item.url
        elif item.named_url:
            item.is_active = request.resolver_match.url_name == item.named_url

    return {'menu': menu}
