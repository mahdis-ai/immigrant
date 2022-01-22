from django import forms
from .models import  Profile
from reservation.models import Applicant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,AbstractUser
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(label = "Password" , widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=100)
    USERNAME_FIELD='phone'
    FILELD_LIST=['username','phone','password']
    class Meta:
        model = User
        fields = ['username','phone','password']

        