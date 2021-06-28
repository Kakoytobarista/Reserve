from django import forms
from .models import Reception
from captcha.fields import CaptchaField


class ReceptionForm(forms.ModelForm):

    class Meta:
        model = Reception
        fields = ['date', 'time_since', 'time_until', 'reserver_name', 'reception_info', 'reserver']

    def __init__(self, *args, **kwargs):
        super(ReceptionForm, self).__init__(*args, **kwargs)

        self.fields['date'].widget.attrs['id'] = 'datepicker'
        self.fields['date'].widget.attrs['autocomplete'] = 'off'
        self.fields['date'].widget.attrs['class'] = 'form-control'

        self.fields['time_since'].widget.attrs['autocomplete'] = 'off'
        self.fields['time_since'].widget.attrs['class'] = 'form-control'
        self.fields['time_since'].widget.attrs['id'] = 'single-input'

        self.fields['time_until'].widget.attrs['autocomplete'] = 'off'
        self.fields['time_until'].widget.attrs['class'] = 'form-control'
        self.fields['time_until'].widget.attrs['id'] = 'single-input_two'

        self.fields['reserver_name'].widget.attrs['autocomplete'] = 'off'
        self.fields['reserver_name'].widget.attrs['class'] = 'form-control'

        self.fields['reception_info'].widget.attrs['autocomplete'] = 'off'
        self.fields['reception_info'].widget.attrs['class'] = 'form-control'


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    photo = forms.ImageField(label='File')
    captcha = CaptchaField()

