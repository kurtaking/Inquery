from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    render(request, 'login.html')