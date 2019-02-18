from django.shortcuts import render

def home(request):
    return render(request, 'stuffsharing/home.html')


def about(request):
    return render(request, 'stuffsharing/about.html')
