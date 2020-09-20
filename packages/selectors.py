from django.db.models import Q
from .models import *


def getCategoryObj(category_slug):
    try:
        return Category.objects.get(slug=category_slug)
    except Category.DoesNotExist:
        return None


def getCategoryTours(category_slug):
    return Tour.objects.filter(category__slug=category_slug)


def getTourBySlug(tour_slug):
    try:
        return Tour.objects.get(slug=tour_slug)
    except Tour.DoesNotExist:
        return None


def getTourDetail(tour_instance):
    try:
        return TourDetail.objects.get(tour=tour_instance)
    except TourDetail.DoesNotExist:
        return None


def getTourItenary(tour_instance):
    return TourItenary.objects.filter(tour__pk=tour_instance.pk)


def getTourAllReviews(tour_slug):
    return Review.objects.filter(tour__slug=tour_slug).order_by('-rating')


def getTourAllHighlights(tour_detail_obj):
    return tour_detail_obj.highlights.split('\n')


def getRelatedTours(category_slug, tour_slug):
    return Tour.objects.filter(~Q(slug=tour_slug), category__slug=category_slug).order_by('-created_at')[:4]
