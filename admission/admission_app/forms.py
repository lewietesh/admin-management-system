import email
from unicodedata import name
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'date_of_birth','gender', 'id_number','disability','image', ]
        

class ApplicationForm(forms.ModelForm):
  
    class Meta:
        model = Application
        exclude = ('user', 'Application_Status', 'message',)

        # fields = [ 'name', 'course', 'email', 'phone_no', 'address', ]