from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from . import constants as user_constants


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=45, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    user_type = models.PositiveSmallIntegerField(choices=user_constants.USER_TYPE, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
