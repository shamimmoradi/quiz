from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.mail import send_mail
from quiz import settings


class UserManager(BaseUserManager):
    def create_user(self, data):
        user = self.create(**data)
        user.set_password(data['password'])
        user.save()
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=20, null=True, blank=True, unique=False)
    last_name = models.CharField(max_length=20, null=True, blank=True, unique=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def send_email(self, subject, content):
        send_mail(
            subject,
            content,
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False,
        )
