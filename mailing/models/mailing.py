from django.conf import settings
from django.db import models

from constants import NULLABLE
from mailing.models.client import Client
from django.utils import timezone


class Message(models.Model):
    subject = models.CharField(max_length=200, verbose_name='тема', **NULLABLE)
    body = models.TextField(verbose_name='текст письма', **NULLABLE)

    def __str__(self):
        return f' Тема: {self.subject}. Содержание: {self.body}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingSettings(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    STATUS_CHOICES = [
        ('created', 'Created'),
        ('started', 'Started'),
        ('completed', 'Completed'),
    ]

    sending_date = models.DateTimeField(verbose_name='дата рассылки', default=timezone.now)

    sending_time = models.TimeField(verbose_name='время рассылки')
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created', verbose_name='статус')

    client = models.ManyToManyField(Client, verbose_name='клиент')  # Связь многие ко многим с моделью Client
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, max_length=150, verbose_name='пользователь')  # Связь многие к одному с моделью User

    # Добавляем поле для связи с сообщением
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='активно')

    def __str__(self):
        clients = ", ".join([client.email for client in self.client.all()])
        return (
            f"Сообщение отправлено для {clients}, "
            f"периодичность рассылки {self.get_frequency_display()}, статус {self.get_status_display()}"
        )

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
