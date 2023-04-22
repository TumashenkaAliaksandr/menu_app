from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Menu


class MenuView(View):
    template_name = 'menu/menu.html'

    def get(self, request, menu_name):
        menu = get_object_or_404(Menu, name=menu_name)
        return render(request, self.template_name, {'menu': menu})
