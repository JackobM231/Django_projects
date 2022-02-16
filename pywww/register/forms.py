from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
  email = forms.EmailField()
  agreement = forms.BooleanField(label="Zapoznałem się z regulaminem", required=True)
  
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    