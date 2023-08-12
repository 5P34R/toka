from django import forms
from .models import Client

class EventRegistrationForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.HiddenInput())
