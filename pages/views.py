from django.shortcuts import render, redirect
from packages.models import Category
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages



def home(request):
    if request.method == 'GET':
        banner = Banner.objects.all()
        packages = Category.objects.all()
        return render(request, 'index.html', {
            'bannner':  banner,
            'packages': packages
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
        query = request.POST.get('query')
        template = render_to_string("contact_us.html",{
            "first_name":first_name,
            "last_name":last_name,
            "email":email,
            "phone":phone,
            "query":query})

        send_mail("customer_query", None, email, [settings.EMAIL_HOST_USER], html_message=template)
        messages.success(request, 'We will revert back you soon')
        return redirect("pages:contact")










