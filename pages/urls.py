from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', home, name='home'),
    path('tours', tours, name='tours'),
    path('about_us', aboutUs, name="about"),
    path('contact_us', contactUs, name="contact"),
    path('query', send_query, name="query"),
    path('faq', faq, name="faq"),
    path('gallery', gallery, name="gallery"),
    path('team_profile', team_profile, name="team_profile")
]