from django.template.loader import render_to_string
from pages.helpers import *
from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import * 
from django.conf import settings


def createTestimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            testimonial = Testimonials.objects.get(name=form.cleaned_data['name'], approved=False)
            template_approval = render_to_string('testimonials_approve.html', {
                'name' : form.cleaned_data['name'],
                'link' : f'http://localhost:8000/admin/testimonials/testimonials/{testimonial.id}/change/'

                })
            sendMail(settings.EMAIL_HOST_USER, template_approval, 'New Review Received')
            return redirect('pages:home')
    else:
        form = TestimonialForm()
    return render(request, 'testimonial_form.html', {
        'form': form
    })
