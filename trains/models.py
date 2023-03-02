from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Номер поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Из города', related_name='from_city_set')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='В город', related_name='to_city_set')

    def __str__(self):
        return f'Поезд №{self.name}'

    def get_absolute_url(self):
        return reverse('trains:detail', kwargs={'pk': self.pk})

    def clean(self):
        errors = {}
        if self.from_city == self.to_city:
            errors['from_city'] = ValidationError('Города совпадают')
            errors['to_city'] = ValidationError('Города совпадают')
        qs = Train.objects.filter(travel_time=self.travel_time, from_city=self.from_city, to_city=self.to_city).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Такой-же маршрут уже существует')
        if errors:
            raise ValidationError(errors)

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['name',]
