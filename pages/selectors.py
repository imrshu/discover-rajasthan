from .models import FAQ


def getAllFaqs():
    return FAQ.objects.all()