from .models import *


def getAllFaqs():
    return FAQ.objects.all()


def getAllGalleryObjs():
    return Gallery.objects.all()


def getAllTeamProfileObjs():
    return TeamProfile.objects.all()