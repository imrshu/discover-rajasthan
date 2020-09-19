from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Review)
admin.site.register(BookNow)

class TourDetailInline(admin.StackedInline):
	model = TourDetail

class TourItenaryInline(admin.StackedInline):
	model = TourItenary

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
	inlines = [TourDetailInline, TourItenaryInline]




		