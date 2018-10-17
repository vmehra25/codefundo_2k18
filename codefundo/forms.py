from django.db import models
from django import forms
from codefundo.models import user_details,User

class input(forms.ModelForm):
    class Meta:
        model = user_details
        fields= '__all__'

class Authentic(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =("username","password","first_name","last_name","email",)


