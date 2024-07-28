from django import forms
from .models import contact , user
from django.contrib.auth.forms import UserCreationForm ,PasswordResetForm
from django.contrib.auth.models import User
class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ("name", "email", "subject", "message")

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ("username", "email", "password",)
        
class RegisterForm(UserCreationForm):
    username = forms.CharField(label=("Username"),help_text="")
    email = forms.EmailField(label = "Email" , help_text="")
    password1 = forms.CharField(label = "Password",help_text="",widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Confirm Password",help_text="",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username","email","password1" , "password2" )    
        
        
class ForgetPasswordForm(PasswordResetForm):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    
    class Meta:
        model = User
        fields = ("username" , "email")
        
class ResetPasswordForm(PasswordResetForm):
    password1 = forms.CharField(label="New Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("password1" , "password2")