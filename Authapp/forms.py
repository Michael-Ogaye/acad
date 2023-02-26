from .models import Cadmin,CustomUser,Professor,Student
from django import forms


class SRegForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('email','phone_number','password')
    

class PRegForm(forms.ModelForm):
    class Meta:
        model=Professor
        fields=('email','phone_number','password')
    