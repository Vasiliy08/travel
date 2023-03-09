from django import forms


class ChartsForm(forms.Form):
    month = forms.CharField(max_length=100)
    qwe = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
