from django import forms
from .models import Subscription


CHOICES = [
    ('7'),
    ('30'),
    ('365'),
]


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ("duration_days",)
        duration_days = forms.ChoiceField(widget=forms.RadioSelect,
                                          choices=CHOICES)
