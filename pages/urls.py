from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', home, name='home'),
    path('about_us', aboutUs, name="about"),
    path('contact_us', contactUs, name="contact"),
]