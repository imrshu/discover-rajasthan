from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from packages.sitemap import *

sitemaps = {
    'static': StaticViewSitemap,
    'category': CategorySitemap,
    'tour': TourSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('testimonials/', include('testimonials.urls', namespace='testimonials')),
    path('packages/', include('packages.urls', namespace='packages')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

