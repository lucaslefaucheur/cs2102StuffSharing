from django.shortcuts import render
from stuffsharing.models import TestUser, TestObject, IsWillingToRent


def home(request):
    return render(request, 'stuffsharing/home.html')


def about(request):
    return render(request, 'stuffsharing/about.html')


