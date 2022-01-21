from django import forms
from .models import  Profile
from django.contrib.auth.models import User
from reservation.models import Applicant
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(label = "Password" , widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Profile
        fields = ['username','phone','password']
        