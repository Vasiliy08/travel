# Generated by Django 4.1.7 on 2023-03-06 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название маршрута')),
                ('travel_time', models.PositiveSmallIntegerField(verbose_name='Общее время в пути')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city', verbose_name='Из города')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city', verbose_name='В город')),
                ('trains', models.ManyToManyField(to='trains.train', verbose_name='Поезда')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
                'ordering': ['name'],
            },
        ),
    ]
