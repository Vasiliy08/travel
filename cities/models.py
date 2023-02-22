from django.db import models
from django.urls import reverse
from pytils.translit import slugify

class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название города')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Идентификатор')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('name', )