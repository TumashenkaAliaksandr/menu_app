from django.shortcuts import render
from django.urls import reverse
from .models import Menu


def draw_main_menu(request):
    menu_items = Menu.objects.all()
    context = {'menu': menu_items}
    return render(request, 'menu.html', context)
