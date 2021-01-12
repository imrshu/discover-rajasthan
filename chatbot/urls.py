from django.urls import re_path
from django.contrib import admin

from .views import (
    FacebookWebhookView,
    )

app_name ='chatbot'

urlpatterns = [
    # replace <string_endpoint> with the one you created above
    re_path(r'^efe66298419c1e7b40e3db9a1ebf7d9a8683cb6f80dfa8157e408bad488a/$', FacebookWebhookView.as_view(), name='webhook'),
]