from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages
from django.views.decorators.cache import cache_page
from .models import *
from .tasks import *
from .selectors import *
from packages.models import *
from testimonials.models import Testimonials


@cache_page(300)
def home(request):
    if request.method == 'GET':
        banner = Banner.objects.all()
        packages = Category.objects.all()
        testimonials = Testimonials.objects.all()
        return render(request, 'index.html', 
        {
            'bannner':  banner,
            'packages': packages,
            'testimonials': testimonials
        })


def tours(request):
    if request.method == 'GET':
        tours = Tour.objects.all()
        categories = Category.objects.all()
        return render(request, 'all_tours.html', {
            'tours' : tours,
            'tours_count': tours.count(),
            'categories' : categories
        })


def aboutUs(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        return render(request, 'about.html', {
            'teams': teams
        })


def contactUs(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')


def send_query(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        code = request.POST.get('code')
        query = request.POST.get('query')

        template = render_to_string("contact_email.html", {
            "first_name":first_name,
            "last_name":last_name,
            "email":email,
            "phone":phone,
            "query":query,
            "code":code
        })

        template1 = render_to_string("contact_inquiry.html", {
            "first_name":first_name,
            "last_name":last_name
        })

        sendMail.delay(email, template, "Customer Query")
        clientMail.delay(email, template1, "Respond from Discover Rajasthan")

        messages.success(request, 'We will revert back you soon')
        return redirect("pages:contact")


def faq(request):
    if request.method == 'GET':
        faqs = getAllFaqs()
        return render(request, 'faq.html', {
            'faqs': faqs
        })


def gallery(request):
    if request.method == 'GET':
        gallery = getAllGalleryObjs()
        return render(request, 'gallery.html', {
            'gallery': gallery
        })


def team_profile(request):
    if request.method == 'GET':
        profiles = getAllTeamProfileObjs()
        return render(request, 'profile.html', {
            'profiles': profiles
        })


def terms_and_conditions(request):
    if request.method == 'GET':
        return render(request, 'terms_of_conditions.html')
