from django import forms
from .models import Task,StudentProfile


class TaskForm (forms.ModelForm):

    class Meta:
        model=Task
        fields='__all__'

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model=StudentProfile
        fields='__all__'
        