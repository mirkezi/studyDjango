from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    class Meta:
        model = forms
        fields = ['username','password']