from django.urls import re_path
from .views import createTestimonial

app_name = 'testimonials'

urlpatterns = [
    re_path(r'create/$', createTestimonial, name='create'),
]