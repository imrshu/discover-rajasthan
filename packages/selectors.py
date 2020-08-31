from .models import Category, Tour


def getCategoryObj(category_slug):
    try:
        return Category.objects.get(slug=category_slug)
    except Category.DoesNotExists:
        return None


def getCategoryTours(category_slug):
    return Tour.objects.filter(category__slug=category_slug)


def getTourTitle(tour_slug):
    try:
        return Tour.objects.get(slug=tour_slug)
    except Tour.DoesNotExists:
        return None


def getCategoryTitle(category_slug):
    try:
        return Category.objects.get(slug=category_slug).title
    except Category.DoesNotExists:
        return None