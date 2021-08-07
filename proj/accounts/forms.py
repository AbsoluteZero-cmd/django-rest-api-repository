from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=255, required=True)
	email = forms.EmailField(required=False)
	password = forms.CharField(widget=forms.PasswordInput, required=True)