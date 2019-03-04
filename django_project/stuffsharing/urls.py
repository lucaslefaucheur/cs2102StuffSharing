from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='stuffsharing-home'),
    path('search/', views.search, name='stuffsharing-search'),
    path('post/', views.post, name='stuffsharing-post'),
    path('about/', views.about, name='stuffsharing-about'),
]