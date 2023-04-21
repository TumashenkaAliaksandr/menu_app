from django.urls import path
from django.conf.urls.static import static

from menu_app import settings
from menu.views import *

app_name = 'menu'

urlpatterns = [
    path('', my_menu, name='my_menu')

]

