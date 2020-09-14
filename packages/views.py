from django.shortcuts import render
from .selectors import *
from .models import *


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
            'category_slug': category_slug,
            'category_image_url': category.image.url
        })


def getTour(request, **kwargs):
    if request.method == 'GET':
        tour = getTourBySlug(kwargs.get('tour_slug'))
        tour_detail = getTourDetail(tour)
        tour_itenary = getTourItenary(tour)


        return render(request, 'package_detail.html', {
            'tour': tour,
            'tour_image_url': tour.image.url,
            'package_title': tour.category.title,
            'tour_detail': tour_detail,
            'tour_itenary': tour_itenary,
            'inclusions' : tour_detail.inclusion.split('\n'),
            'exclusions' : tour_detail.exclusion.split('\n'),
        })




