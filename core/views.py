from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import BlogPost
from core.services import get_cached_clients
from mailing.models.client import Client
from mailing.models.mailing import MailingSettings


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['mailing'] = MailingSettings.objects.all()
            context['client'] = Client.objects.all()
        context['client'] = get_cached_clients(user=self.request.user)
        context['mailing'] = MailingSettings.objects.filter(user=self.request.user)

        all_blogs = BlogPost.objects.all()
        # random_blogs = sample(list(all_blogs), 3)

        # context['blog'] = random_blogs
        return context


class GuestPageView(TemplateView):
    template_name = 'core/home_guest.html'


def contacts_view(request):
    return render(request, 'core/contacts.html')
