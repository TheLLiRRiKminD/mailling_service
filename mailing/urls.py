from django.urls import path

from mailing.views.client import ClientCreateView, ClientListView, ClientDetailView, ClientDeleteView, ClientUpdateView
from mailing.views.mailing import MailingSettingsCreateView, MailingSettingsListView, MailingSettingsDetailView, \
    MailingSettingsUpdateView, MailingSettingsDeleteView
from mailing.views.mailing_log import MailingLogListView

app_name = 'mailing'

urlpatterns = [
    path('', MailingSettingsListView.as_view(), name='mailingsettings_list'),
    path('create/', MailingSettingsCreateView.as_view(), name='mailingsettings_create'),
    path('detail/<int:pk>/', MailingSettingsDetailView.as_view(), name='mailingsettings_detail'),
    path('update/<int:pk>/', MailingSettingsUpdateView.as_view(), name='mailingsettings_update'),
    path('delete/<int:pk>/', MailingSettingsDeleteView.as_view(), name='mailingsettings_delete'),

    path('mailinglog/', MailingLogListView.as_view(), name='mailing_log'),

    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/list/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
]

