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


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'FAQ\"s'

    def __str__(self):
        return self.question


class Gallery(models.Model):
    image = ResizedImageField(size=[800, 533], upload_to='gallery')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.image.path


class TeamProfile(models.Model):
    title = models.CharField(max_length=20)
    bio = models.TextField()
    bio_pic = models.ImageField(upload_to='team_profile')
    facebook_link = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Team Profile'
    
    def __str__(self):
        return self.title
    