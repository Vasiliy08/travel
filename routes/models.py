from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from cities.models import City
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название маршрута')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Общее время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Из города', related_name='route_from_city_set')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='В город', related_name='route_to_city_set')
    trains = models.ManyToManyField(Train, verbose_name='Поезда')

    def __str__(self):
        return f'Маршрут {self.name} из города {self.from_city}'

    def get_absolute_url(self):
        return reverse('routes:detail', kwargs={'pk': self.pk})

    def clean(self):
        errors = {}
        if self.from_city == self.to_city:
            errors['from_city'] = ValidationError('Города совпадают')
            errors['to_city'] = ValidationError('Города совпадают')
        if errors:
            raise ValidationError(errors)

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['name',]
