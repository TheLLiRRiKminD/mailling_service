# core/templatetags/custom_filters.py

from django import template
from django.template.defaultfilters import truncatechars
from django.templatetags.static import static
from django.conf import settings

register = template.Library()


@register.filter
def mediapath(image_path):
    # Формируем полный путь к медиафайлу, добавляя префикс '/media/'
    media = settings.MEDIA_URL
    return f"{media}{image_path}"


@register.filter
def truncate_description(description, length=100):
    # Обрезаем описание до первых 100 символов
    return truncatechars(description, length)
