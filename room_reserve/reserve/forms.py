from django import forms
from django.contrib.admin import widgets

from .models import Rooms, Reception


class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ('date', 'time', 'reception_info')

    def __init__(self, *args, **kwargs):
        super(ReceptionForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = forms.HiddenInput()
        self.fields['reception_info'].widget = forms.Textarea(attrs={'cols': 60, 'rows': 8})
        self.fields['reception_info'].label = 'Info about reserve'
