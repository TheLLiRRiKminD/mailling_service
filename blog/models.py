from django.conf import settings
from django.db import models

from constants import NULLABLE


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', **NULLABLE)
    views_count = models.PositiveIntegerField(default=0)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title} created:{self.publication_date}'

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
