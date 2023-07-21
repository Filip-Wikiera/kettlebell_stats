from django.forms import ModelForm
from django import forms
from .models import Session


class SessionFrom(ModelForm):
    class Meta:
        model = Session
        fields = ["exercise", "rep_count", "weight", "date", "bottom_up", "hand", "description"]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
