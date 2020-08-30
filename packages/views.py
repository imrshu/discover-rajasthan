from django.shortcuts import render
from .models import Category, Tour


def getCategory(request, **kwargs):
    if request.method == 'GET':
        category = Category.objects.get(slug=kwargs.get('slug'))
        tours = Tour.objects.filter(category__slug=kwargs.get('slug'))
        return render(request, 'package_tours.html', {
            'tours': tours,
            'package_name': category.title,
            'package_desc': category.description
        })