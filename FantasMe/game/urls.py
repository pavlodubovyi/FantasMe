from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_character/', views.create_character, name='create_character'),
]