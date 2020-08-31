from django.shortcuts import render
from .selectors import *


def getCategory(request, **kwargs):
    if request.method == 'GET':
        category_slug = kwargs.get('slug')
        category = getCategoryObj(category_slug)
        tours = getCategoryTours(category_slug)
        return render(request, 'package_tours.html', {
            'tours': tours,
            'tours_count': tours.count(),
            'package_name': category.title,
            'package_desc': category.description,
            'category_slug': category_slug
        })


def getTour(request, **kwargs):
    if request.method == 'GET':
        return render(request, 'package_detail.html', {
            'tour_title': getTourTitle(kwargs.get('tour_slug')),
            'package_title': getCategoryTitle(kwargs.get('category_slug'))
        })
