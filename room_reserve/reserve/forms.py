from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Login


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Login
#         fields = ('login', 'password')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save person'))

