from django import forms
from .models import *


class WeatherForm(forms.Form):
    city_field = forms.CharField(max_length=40)

