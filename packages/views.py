from django.shortcuts import render
from .selectors import *


def getCategory(request, **kwargs):
    if request.method == 'GET':
        slug = kwargs.get('slug')
        category = getCategoryObj(slug)
        tours = getCategoryTours(slug)
        return render(request, 'package_tours.html', {
            'tours': tours,
            'tours_count': tours.count(),
            'package_name': category.title,
            'package_desc': category.description
        })