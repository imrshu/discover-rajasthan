from django.db import models
from django_resized import ResizedImageField


class Team(models.Model):
    image = ResizedImageField(size=[458, 540], upload_to='team')
    name = models.CharField(max_length=40)
    mobile = models.CharField(max_length=10)
    position = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Team'
    
    def __str__(self):
        return self.name


class Banner(models.Model):
    image = ResizedImageField(size=[1600, 667], upload_to='banner')
    place_name = models.CharField(max_length=30)
    tagline = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Banner'
    
    def __str__(self):
        return self.place_name