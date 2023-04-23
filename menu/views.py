from django.shortcuts import render
from .models import Menu


def draw_main_menu(request):
    """
       Возвращает шаблон 'menu.html', содержащий список пунктов главного меню.
       Аргументы:
       - request: объект запроса Django.
       Возвращает:
       - объект ответа Django, содержащий шаблон и контекст для него.
    """
    menu_items = Menu.objects.all()
    context = {'menu': menu_items}
    return render(request, 'menu.html', context)
