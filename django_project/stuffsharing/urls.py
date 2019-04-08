from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='stuffsharing-home'),
    path('search/', views.search, name='stuffsharing-search'),
    path('myadsadd/', views.myadsadd, name='stuffsharing-myadsadd'),
    path('myadsactive/', views.myadsactive, name='stuffsharing-myadsactive'),
    path('myadsinactive/', views.myadsinactive, name='stuffsharing-myadsinactive'),
    path('myrequests/', views.myrequests, name='stuffsharing-myrequests'),
    path('currenttransactions/', views.currenttransactions, name='stuffsharing-currenttransactions'),
    path('about/', views.about, name='stuffsharing-about'),
    path('myaccount/', views.myaccount, name='stuffsharing-myaccount'),
    path('signup/',views.signup,name='stuffsharing-signup'),

]
