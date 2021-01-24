from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *


class CategorySitemap(Sitemap):
    changefreq = 'yearly'

    def items(self):
        return Category.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at


class TourSitemap(Sitemap):
    changefreq = 'weekly'

    def items(self):
        return Tour.objects.filter(is_active=True)
    
    def lastmod(self, obj):
        return obj.updated_at


class StaticViewSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return ['pages:home', 'pages:tours', 'pages:about', 'pages:contact', 'pages:faq', 
        'pages:gallery', 'pages:team_profile', 'pages:terms_and_conditions']
    
    def location(self, item):
        return reverse(item)
