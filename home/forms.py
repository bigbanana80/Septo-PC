from django import forms
from .models import contact , user


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ("name", "email", "subject", "message")

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ("username", "email", "password",)