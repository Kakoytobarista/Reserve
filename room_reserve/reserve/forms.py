from django import forms


class ReceptionForm(forms.Form):
    date_of_reserve = forms.SelectDateWidget()
    time = forms.SplitDateTimeWidget()
    info_about_reserve = forms.Textarea()

