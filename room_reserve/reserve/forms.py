from django import forms
from .models import Reception


class ReceptionForm(forms.ModelForm):

    class Meta:
        model = Reception
        fields = ['date', 'time', 'reserver_name', 'reception_info', 'reserver']
        widgets = {
            'date': forms.DateInput(),
            'time': forms.TimeInput(),

        }
