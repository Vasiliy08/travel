from django import forms

from cities.models import City
from routes.models import Route


class RouteForm(forms.ModelForm):
    from_city = forms.ModelChoiceField(label='Из города', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}))
    to_city = forms.ModelChoiceField(label='В город', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}))
    cities = forms.ModelMultipleChoiceField(label='Через города', queryset=City.objects.all(), required=False, widget=forms.SelectMultiple(
        attrs={'class': 'form-control js-example-basic-multiple'}
    ))
    travel_time = forms.IntegerField(label='Время', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите время в пути'}))

    class Meta:
        model = Route
        fields = ('travel_time', 'from_city', 'to_city', 'cities')