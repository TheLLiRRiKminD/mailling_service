from django.urls import path
from core.apps import CoreConfig
from core.views import HomePageView, GuestPageView, contacts_view

app_name = CoreConfig.name

urlpatterns = [
    path('', GuestPageView.as_view(), name='guest'),
    path('core/', HomePageView.as_view(), name='index'),
    path('contacts/', contacts_view, name='contacts'),
]
