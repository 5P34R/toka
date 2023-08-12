from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Company

class ClientRegistrationForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ('email', 'password1', 'password2', 'mobile', 'dob', 'country')

class CompanyRegistrationForm(UserCreationForm):
    class Meta:
        model = Company
        fields = ('email', 'password1', 'password2', 'name', 'phone', 'location', 'category')
