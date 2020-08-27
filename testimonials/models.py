from django.db import models


class Testimonials(models.Model):
    name = models.CharField(max_length=30)
    review = models.TextField()
    image = models.ImageField(upload_to='testimonials')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Clients'
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.name
