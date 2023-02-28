from .models import Cadmin,CustomUser,Professor,Student
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class SRegForm(forms.ModelForm):
   
    class Meta:
        model=Student
        fields=('email','phone_number','username','password')
    

class PRegForm(forms.ModelForm):
    
    class Meta:
        model=Professor
        fields=('email','phone_number','username','password')
    

class SignForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('email','password')