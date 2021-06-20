from django import forms
from .models import Reception
from captcha.fields import CaptchaField


class ReceptionForm(forms.ModelForm):

    class Meta:
        model = Reception
        fields = ['date', 'time', 'reserver_name', 'reception_info', 'reserver']
        widgets = {
            'date': forms.DateInput(),
            'time': forms.TimeInput(),

        }


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    captcha = CaptchaField()

