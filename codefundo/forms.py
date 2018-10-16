from django.db import models
from django import forms
from codefundo.models import user_details

class input(forms.ModelForm):
    class Meta:
        model = user_details
        fields= '__all__'
