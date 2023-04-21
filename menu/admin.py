from django.contrib import admin
from menu.models import MenuItem, Menu


class MenuItemAdmin(admin.ModelAdmin):
    """
    Класс для кастомизации админки для модели MenuItem.
    """
    list_display = ('name', 'url', 'parent')
    list_filter = ('parent',)
    search_fields = ('name', 'url')


class MenuAdmin(admin.ModelAdmin):
    """
    Класс для кастомизации админки для модели Menu.
    """
    list_display = ('name',)


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)
