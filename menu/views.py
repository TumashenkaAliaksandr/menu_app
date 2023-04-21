from django.shortcuts import render, get_object_or_404
from menu.models import Menu

def my_menu(request):
    menu = get_object_or_404(Menu, name='my_menu')
    context = {
        'menu': menu,
    }
    return render(request, 'my_template.html', context)

