from django import forms
from django.forms import formset_factory, modelformset_factory

from .models import Chart


class ChartsForm(forms.Form):
    qwe = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))

class ChartForm2(forms.ModelForm):
    class Meta:
        model = Chart
        fields = '__all__'


ChartFormSet = formset_factory(ChartForm2, extra=2)

ChartFormSet2 = modelformset_factory(Chart, fields=('name_q',), exclude=('id',),extra=2, formset=ChartForm2)