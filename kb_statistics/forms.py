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


class MonthPicker(forms.Form):
    months = [
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    ]
    years = [year for year in range(2020, 2030)]

    month = forms.ChoiceField(choices=months, label='Month')
    year = forms.ChoiceField(choices=[(year, year) for year in years], label='Year')
