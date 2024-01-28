from django import forms
from django.forms import modelformset_factory

from .models.mailing import Message, MailingSettings
from .models.mailing_log import MailingLog
from .models.client import Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingLogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingLog
        fields = '__all__'


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingSettings
        fields = '__all__'
        # fields = ['sending_time', 'frequency', 'status', 'user', 'is_active']  # Включите поля, которые вы хотите отображать

    message_subject = forms.CharField(max_length=200, required=True, label='Тема сообщения')
    message_body = forms.CharField(widget=forms.Textarea, required=True, label='Текст сообщения')

    # Убедитесь, что поле 'is_active' определено и имеет правильное имя и виджет
    is_active = forms.BooleanField(required=False, initial=True, label='Активно')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['message_subject'].widget.attrs.update({'class': 'form-control'})
        self.fields['message_body'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})  # Устанавливаем класс для стилизации чекбокса


MessageFormSet = modelformset_factory(Message, form=MessageForm, extra=1)
