from django.shortcuts import render, redirect
from .selectors import *
from .models import *
from pages.helpers import *


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
        reviews = Review.objects.all().order_by('-rating')
        highlights = tour_detail.highlights.split('\n') 


        return render(request, 'package_detail.html', {
            'tour': tour,
            'tour_image_url': tour.image.url,
            'package_title': tour.category.title,
            'tour_detail': tour_detail,
            'tour_itenary': tour_itenary,
            'inclusions' : tour_detail.inclusion.split('\n'),
            'exclusions' : tour_detail.exclusion.split('\n'),
            'reviews' : reviews,
            'highlights' : highlights,

        })

def writeReview(request, **kwargs):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        review = request.POST.get('review')

        Review.objects.create(
            tour = Tour.objects.get(slug=kwargs.get('tour_slug')),
            name = name,
            email = email,
            rating = rating,
            review = review
            )
        return redirect("packages:tour", 
            category_slug=kwargs.get('category_slug'),
            tour_slug=kwargs.get('tour_slug') )


def bookNow(request, **kwargs):
    if request.method == 'POST':
        date = request.POST.get('travel_date')
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        people = request.POST.get('people')

        BookNow.objects.create(
            tour = getTourBySlug(kwargs.get('tour_slug')),
            travel_date = date,
            name = name,
            email = email,
            mobile = mobile,
            no_of_people = people
            )
        sendMail(email, None , "Booking Enquiry")

        return redirect("packages:tour",
            category_slug=kwargs.get('category_slug'),
            tour_slug=kwargs.get('tour_slug'))











