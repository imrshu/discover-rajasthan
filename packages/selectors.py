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


def review(**kwargs):
    Review.objects.create(**kwargs)



    # tour = getTourBySlug(kwargs.get('tour_slug'))
    # Review.objects.create(
    #     tour = tour,
    #     name = kwargs.get('name'),
    #     email = kwargs.get('email'),
    #     rating = kwargs.get('rating'),
    #     review = kwargs.get('review')
    #     )


















