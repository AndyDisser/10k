import datetime
from django import forms

from django.forms import ModelForm

from .models import Timestamp

class DateInput(forms.DateInput):
    """Makes the HTML5 Date Input usable."""

    input_type = 'date'


class TimestampForm(forms.ModelForm):
    date = forms.DateField(initial=datetime.date.today(), widget=DateInput)

    class Meta:
        model = Timestamp
        fields = [
            "subject",
            "date",
            "time_spend"
        ]
        # widgets = {"date": DateInput()}
        # initial= {"date": datetime.date.today()}
