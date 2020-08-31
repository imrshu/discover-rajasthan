from .models import Category, Tour


def getCategoryObj(slug):
    try:
        return Category.objects.get(slug=slug)
    except Category.DoesNotExists:
        return None


def getCategoryTours(slug):
    return Tour.objects.filter(category__slug=slug)
