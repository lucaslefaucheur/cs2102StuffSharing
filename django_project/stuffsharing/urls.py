from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='stuffsharing-home'),
    path('about/', views.about, name='stuffsharing-about'),
]