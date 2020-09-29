from .models import *


def saveReview(*args, **kwargs):
    Review.objects.create(**kwargs)


def saveBooking(*args, **kwargs):
    BookNow.objects.create(**kwargs)
