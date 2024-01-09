from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    photo = models.ImageField(upload_to='users')
