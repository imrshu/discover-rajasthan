from django.shortcuts import render, redirect
from packages.models import *
from .models import *
from django.template.loader import render_to_string
from django.contrib import messages
from testimonials.models import Testimonials
from .helpers import *


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
        return render(request, 'grid.html', {
            'tours' : tours
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

        sendMail(email, template, "Customer Query")
        messages.success(request, 'We will revert back you soon')
        return redirect("pages:contact")


def faq(request):
    if request.method == 'GET':
        return render(request, 'faq.html')