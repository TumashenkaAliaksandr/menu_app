from django.conf.urls.static import static

from menu_app import settings
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/main_menu/', permanent=False)),

]

