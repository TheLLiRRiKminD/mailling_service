from django.views.generic import ListView

from mailing.models.mailing_log import MailingLog


class MailingLogListView(ListView):
    model = MailingLog
    context_object_name = 'mailing_logs'

    def get_queryset(self):
        if self.request.user.is_staff:
            return MailingLog.objects.all()
        queryset = MailingLog.objects.filter(mailing__user=self.request.user)
        return queryset

