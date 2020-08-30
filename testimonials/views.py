from django.shortcuts import render, redirect
from .forms import TestimonialForm


def createTestimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
    else:
        form = TestimonialForm()
    return render(request, 'testimonial_form.html', {
        'form': form
    })
