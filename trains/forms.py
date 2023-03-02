from django import forms

from cities.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Город', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите название города'}))
    travel_time = forms.IntegerField(label='Время', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите время в пути'}))
    from_city = forms.ModelChoiceField(label='Из города', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))
    to_city = forms.ModelChoiceField(label='В город', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Train
        fields = ('name', 'travel_time', 'from_city', 'to_city')