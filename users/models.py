from django.contrib.auth.models import AbstractUser
from django.db import models

from constants import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='e-mail')

    avatar = models.ImageField(upload_to='user/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)

    is_active = models.BooleanField(default=False, verbose_name='Почта подтверждена')
    email_verification_token = models.CharField(max_length=255, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

        permissions = [
            ('can_change_user_is_active', 'Can change user is active'),
        ]

