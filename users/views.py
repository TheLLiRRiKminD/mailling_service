import secrets

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        new_user = form.save()
        new_user.email_verification_token = secrets.randbelow(1_000_000)
        new_user.save()

        token = urlsafe_base64_encode(force_bytes(new_user.email_verification_token))
        verification_url = reverse('users:verify', kwargs={'token': token})
        send_mail(
            subject='Регистрация на Портале.',
            message=f'Для подтверждения регистрации, пройдите по ссылке ниже в письме. \n {self.request.build_absolute_uri(verification_url)}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def verify_email(request, token):
    try:
        user_verification_key = urlsafe_base64_decode(token).decode()
        user = User.objects.get(email_verification_token=user_verification_key)
        if user_verification_key == user.email_verification_token:
            user.is_active = True
            user.save()
            return redirect('core:index')
        else:
            return render(request, 'users/verification_failure.html')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return render(request, 'users/verification_failure.html')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("core:index")

    def get_object(self, queryset=None):
        return self.request.user

