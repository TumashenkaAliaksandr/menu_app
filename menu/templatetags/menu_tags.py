from django import template
from menu.models import Menu


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """
    Функция для отображения меню на странице.
    """
    request = context['request']
    current_url = request.path
    menu_items = Menu.objects.get(name=menu_name).items.all()

    def generate_menu_html(items):
        """
        Вспомогательная функция для генерации HTML-кода меню.
        """
        html = '<ul>'
        for item in items:
            is_active = current_url == item.get_absolute_url()
            item_html = f'<li class="{"active" if is_active else ""}">'
            item_html += f'<a href="{item.get_absolute_url()}">{item.name}</a>'
            if item.children.exists():
                item_html += generate_menu_html(item.children.all())
            item_html += '</li>'
            html += item_html
        html += '</ul>'
        return html

    menu_html = generate_menu_html(menu_items)
    return menu_html
