from django import template
from django.db.models import Q
from menu.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.filter(Q(name=menu_name) | Q(parent__name=menu_name)).order_by('parent__id', 'id')

    def make_tree(menu, parent=None):
        tree = []
        for item in menu:
            if item.parent == parent:
                children = make_tree(menu, item)
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
