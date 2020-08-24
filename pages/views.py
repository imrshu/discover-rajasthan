from django.shortcuts import render
from .models import *


def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def aboutUs(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        return render(request, 'about.html', {
            'teams': teams
        })


def contactUs(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
