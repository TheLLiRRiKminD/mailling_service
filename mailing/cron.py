from datetime import datetime

from mailing.models.mailing import MailingSettings
from mailing.services import send_mailing


def daily_send():
    now = datetime.now()
    for mailing in MailingSettings.objects.filter(frequency='daily', sending_time=now.time(), sending_date=now.date()):
        mailing.status = 'started'
        mailing.save()
        log = send_mailing(mailing)
        mailing.status = 'completed'
        mailing.save()


def weekly_send():
    now = datetime.now()
    for mailing in MailingSettings.objects.filter(frequency='weekly',  sending_time=now.time(), sending_date=now.date()):
        mailing.status = 'started'
        mailing.save()
        log = send_mailing(mailing)
        mailing.status = 'completed'
        mailing.save()


def monthly_send():
    now = datetime.now()
    for mailing in MailingSettings.objects.filter(frequency='monthly',  sending_time=now.time(), sending_date=now.date()):
        mailing.status = 'started'
        mailing.save()
        log = send_mailing(mailing)
        mailing.status = 'completed'
        mailing.save()
