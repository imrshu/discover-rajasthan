from django.db import models


class Team(models.Model):
    image = models.ImageField(upload_to='team')
    name = models.CharField(max_length=40)
    mobile = models.CharField(max_length=10)
    position = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Team'
    
    def __str__(self):
        return self.name