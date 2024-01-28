from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from mailing.forms import ClientForm
from mailing.models.client import Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        if self.request.user.is_staff:
            return Client.objects.all()
        queryset = Client.objects.filter(user=self.request.user)
        return queryset


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.user == self.request.user:
            raise Http404()
        return obj


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('core:index')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.user == self.request.user:
            raise Http404()
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            self.object.delete()
            return self.success_url
        else:
            raise Http404()


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('core:index')
