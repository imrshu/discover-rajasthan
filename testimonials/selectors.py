from .models import Testimonials


def getTestimonial(testimonial_name):
    try:
        return Testimonials.objects.get(name=testimonial_name, approved=False)
    except:
        return None