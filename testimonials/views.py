from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect
from pages.tasks import sendMail
from .forms import TestimonialForm
from .models import *
from .selectors import getTestimonial


def createTestimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            testimonial = getTestimonial(form.cleaned_data['name'])
            template_approval = render_to_string('testimonials_approve.html', {
                'name' : form.cleaned_data['name'],
                'link' : f'{request.build_absolute_uri("/")[:-1]}/admin/testimonials/testimonials/{testimonial.id}/change/'
            })

            sendMail.delay(settings.EMAIL_HOST_USER, template_approval, 'New Review Received')
            return redirect('pages:home')
    else:
        form = TestimonialForm()
    return render(request, 'testimonial_form.html', {
        'form': form
    })
