from django.contrib import admin
from .models.mailing import Message, MailingSettings
from .models.mailing_log import MailingLog
from .models.client import Client

admin.site.register(Client)
admin.site.register(MailingLog)
admin.site.register(Message)
admin.site.register(MailingSettings)
