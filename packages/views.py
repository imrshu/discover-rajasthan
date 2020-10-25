from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.db.models import Q
from .selectors import *
from .models import *
from .services import *
from pages.tasks import *


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
        reviews = getTourAllReviews(kwargs.get('tour_slug'))
        highlights = getTourAllHighlights(tour_detail)
        related_tours = getRelatedTours(kwargs.get('category_slug'), kwargs.get('tour_slug'))

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
            'related_tours': related_tours
        })


def writeReview(request, **kwargs):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        review = request.POST.get('review')

        review_data = {
            'tour': getTourBySlug(kwargs.get('tour_slug')),
            'name': name,
            'email': email,
            'rating': rating,
            'review': review
        }

        saveReview(**review_data)

        return redirect("packages:tour",
            category_slug=kwargs.get('category_slug'),
            tour_slug=kwargs.get('tour_slug')
        )


def bookNow(request, **kwargs):
    if request.method == 'POST':
        date = request.POST.get('travel_date')
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        people = request.POST.get('people')

        tour = getTourBySlug(kwargs.get('tour_slug'))

        booknow_form_data = {
            'tour': tour,
            'travel_date': date,
            'name': name,
            'email': email,
            'mobile': mobile,
            'no_of_people': people
        }

        saveBooking(**booknow_form_data)

        booknow_template = render_to_string('tour_booking_email.html', {
            'tour_name': booknow_form_data['tour'].title,
            'package_name': booknow_form_data['tour'].category.title,
            'name': name,
            'travel_date': date,
            'no_of_people': people,
            'mobile': mobile,
            'email': email
        })

        confirmation_template = render_to_string('booking_confirmation.html', {
            'name' : name,
            'tour' : booknow_form_data['tour'].title,
            'duration' : date,
            'persons' : people,
            'cost' : tour.tourdetail.price,
            'inclusions' : tour.tourdetail.inclusion.split('\n'),
            'exclusions' : tour.tourdetail.exclusion.split('\n'),
        })

        sendMail.delay(email, booknow_template, "Booking Enquiry")
        clientMail.delay(email, confirmation_template, "EpicRajasthanTours Confirmation")

        return redirect("packages:tour",
            category_slug=kwargs.get('category_slug'),
            tour_slug=kwargs.get('tour_slug')
        )


def searchTour(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        tours = search_tour(query)
        return render(request, 'searched_tours.html', {
            'tours': tours,
            'q': query
        })


def filter_tours(request):
    if request.method == 'GET': 
        # get categories
        categories = Category.objects.all()
        # set price range
        price_range = None
        # set the filtered tours
        tours = None
        # get form values
        price = request.GET.get('price')
        location = request.GET.get('location')
        theme = request.GET.get('theme')

        if price == "" or price is None:
            price_range = None
            if location is None or location == '':
                tours = Tour.objects.filter(Q(category__title__iexact=theme))
            else:
                if theme is None or theme == '':
                    tours = Tour.objects.filter(Q(location__search=location))
                else:
                    tours = Tour.objects.filter(Q(location__search=location) & Q(category__title__iexact=theme))
        else:
            price_range = [int(price) for price in price.split(',')]
            if location is None or location == '':
                if theme is None or theme == '':
                    tours = Tour.objects.filter(Q(price__range=price_range))
                else:
                    tours = Tour.objects.filter(Q(price__range=price_range) & Q(category__title__iexact=theme))
            else:
                if theme is None or theme == '':
                    tours = Tour.objects.filter(Q(price__range=price_range) & Q(location__search=location))
                else:
                    tours = Tour.objects.filter(Q(price__range=price_range) & Q(location__search=location) & Q(category__title__iexact=theme))

        return render(request, 'all_tours.html', {
            'tours' : tours,
            'tours_count': tours.count(),
            'categories' : categories
        })



