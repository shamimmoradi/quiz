from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=20, null=True, blank=True, unique=False)
    last_name = models.CharField(max_length=20, null=True, blank=True, unique=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
