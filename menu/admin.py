from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'title', 'url', 'named_url', 'is_active')
    list_filter = ('name',)
    search_fields = ('name', 'title', 'url', 'named_url')
    ordering = ('name', 'parent__id', 'id')
