from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def category(request):
    return render(request, 'category.html')


def flash_card(request):
    return render(request, 'flash_card.html')