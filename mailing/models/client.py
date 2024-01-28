from django.db import models
from constants import NULLABLE


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)
    user = models.ForeignKey('users.User', verbose_name='владелец', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.full_name} {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
