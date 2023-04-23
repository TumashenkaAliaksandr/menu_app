from django import template
from django.urls import path
from .views import draw_main_menu
from .templatetags import menu_tags


urlpatterns = [
    path('', draw_main_menu, name='menu'),
]

register = template.Library()
register.inclusion_tag('menu.html', takes_context=True)(menu_tags.draw_main_menu)
