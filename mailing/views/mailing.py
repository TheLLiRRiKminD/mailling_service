from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.forms import MailingSettingsForm, MessageFormSet
from mailing.models.mailing import MailingSettings, Message


class MailingSettingsListView(LoginRequiredMixin, ListView):
    model = MailingSettings
    template_name = 'mailingsettings_list.html'

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.has_perm('mailing.view_mailsettings'):
            return MailingSettings.objects.all()
        queryset = MailingSettings.objects.filter(user=self.request.user, is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_mailings"] = self.object_list.count()
        context["active_count"] = self.object_list.filter(status="started").count()
        return context


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings
    template_name = 'mailingsettings_detail.html'

    def get_object(self, queryset=None):
        # Вместо get_object_or_404 вы можете использовать другие методы получения объекта
        return get_object_or_404(MailingSettings, pk=self.kwargs['pk'])


class MailingSettingsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:mailingsettings_list')
    permission_required = 'mailing.change_mailingsettings'

    def has_permission(self):
        obj = self.get_object()
        if self.request.user == obj.user or self.request.user.is_staff:
            return True
        return super().has_permission()


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('home:index')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404()
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            self.object.delete()
            return self.success_url
        else:
            raise Http404()


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:mailingsettings_list')

    def form_valid(self, form):
        # Сохраняем форму рассылки
        form.instance.user = self.request.user

        # Создаем экземпляр формсета для сообщений
        message_formset = MessageFormSet(self.request.POST)

        if message_formset.is_valid():
            # Если формсет сообщений валиден, сохраняем сообщения
            messages = message_formset.save(commit=False)
            for message in messages:
                message.save()

            # Привязываем сообщения к рассылке
            form.instance.message.set(messages)
        return super().form_valid(form)


