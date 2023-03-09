# Generated by Django 4.1.7 on 2023-03-02 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('slug', models.CharField(default='question', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charts.question')),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_q', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('date', models.DateField(blank=True, max_length=100, null=True, verbose_name='Дата')),
                ('field_0', models.PositiveSmallIntegerField()),
                ('field_1', models.PositiveSmallIntegerField()),
                ('field_2', models.PositiveSmallIntegerField()),
                ('field_3', models.PositiveSmallIntegerField()),
                ('field_4', models.PositiveSmallIntegerField()),
                ('field_5', models.PositiveSmallIntegerField()),
                ('field_6', models.PositiveSmallIntegerField()),
                ('field_7', models.PositiveSmallIntegerField()),
                ('field_8', models.PositiveSmallIntegerField()),
                ('field_9', models.PositiveSmallIntegerField()),
                ('field_10', models.PositiveSmallIntegerField()),
                ('field_11', models.PositiveSmallIntegerField()),
                ('field_12', models.PositiveSmallIntegerField()),
                ('field_13', models.PositiveSmallIntegerField()),
                ('field_14', models.PositiveSmallIntegerField()),
                ('field_15', models.PositiveSmallIntegerField()),
                ('field_16', models.PositiveSmallIntegerField()),
                ('field_17', models.PositiveSmallIntegerField()),
                ('field_18', models.PositiveSmallIntegerField()),
                ('field_19', models.PositiveSmallIntegerField()),
                ('field_20', models.PositiveSmallIntegerField()),
                ('field_21', models.PositiveSmallIntegerField()),
                ('field_22', models.PositiveSmallIntegerField()),
                ('field_23', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'График',
                'verbose_name_plural': 'Графики',
                'ordering': ['name_q'],
                'unique_together': {('name_q', 'date')},
            },
        ),
    ]
