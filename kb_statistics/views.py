from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def index(request):
    context = {
        'welcome_message': 'Witaj w naszej aplikacji!'
    }
    return render(request, 'index.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)
