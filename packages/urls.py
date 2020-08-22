from django.urls import path
from .views import *

app_name = "packages"

urlpatterns = [
    path('', home, name="home"),
]


