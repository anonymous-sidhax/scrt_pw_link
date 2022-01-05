from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('send-pass', views.get_secret_link, name='get_secret_link'),
]