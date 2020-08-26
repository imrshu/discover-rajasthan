from django.shortcuts import render
from packages.models import Category
from .models import *


def home(request):
    if request.method == 'GET':
        banner = Banner.objects.all()
        packages = Category.objects.all()
        return render(request, 'index.html', {
            'bannner':  banner,
            'packages': packages
        })


def aboutUs(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        return render(request, 'about.html', {
            'teams': teams
        })


def contactUs(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
