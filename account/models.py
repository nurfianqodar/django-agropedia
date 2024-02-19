from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True
    )

    EMAIL_FIELD = 'email'
