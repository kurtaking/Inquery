from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, Http404, HttpRequest, HttpResponse
import json
from models import *


def login(request):
    return render(request, 'login.html')


def verify_login(request):
    if request.POST:
        usr = authenticate(username=request.POST['email'], password=request.POST['password'])
        response_data = {}
        if usr is not None:
            # A backend authenticated the credentials
            response_data['valid'] = 'true'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            # No backend authenticated the credentials
            response_data['valid'] = 'false'
            return HttpResponse(json.dumps(response_data), content_type="application/json")

    return HttpResponseRedirect('/login/')


def dashboard(request):
    return render(request, 'dashboard.html')


def category(request):
    return render(request, 'category.html')


def flash_card(request):
    return render(request, 'flash_card.html')
