from django.db import models

from mailing.models.client import Client
from mailing.models.mailing import MailingSettings


class MailingLog(models.Model):
    STATUS_CHOICES = [
        ('success', 'Success'),
        ('error', 'Error'),
        ('pending', 'Pending'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    response = models.TextField()
    mailing = models.ForeignKey(MailingSettings, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылки'

    def __str__(self):
        return f"Log for {self.mailing.client.full_name} at {self.timestamp}"
