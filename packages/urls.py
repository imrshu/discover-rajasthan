from django.urls import path
from .views import *

app_name = "packages"

urlpatterns = [
    path('category/<slug>/tours/', getCategory, name='category'),
    path('category/<category_slug>/tours/<tour_slug>/', getTour, name='tour'),
    path('category/<category_slug>/tours/<tour_slug>/write_review/', writeReview, name='review'),
]