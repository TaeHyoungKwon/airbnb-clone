from django.contrib.auth.models import AbstractUser
from django.db import models

from users.constants import GENDER_CHOICES, LANGUAGE_CHOICES, CURRENCY_CHOICES


class User(AbstractUser):
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="")
    birth_date = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    is_super_host = models.BooleanField(default=False)
