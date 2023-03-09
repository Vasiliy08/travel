from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, Q

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    slug = models.CharField(max_length=10, unique=True,
                            default="question")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Chart(models.Model):
    name_q = models.CharField(max_length=100, verbose_name="Имя", blank=True)
    date = models.DateField(max_length=100,verbose_name="Дата", null=True, blank=True)
    field_0 = models.PositiveSmallIntegerField()
    field_1 = models.PositiveSmallIntegerField()
    field_2 = models.PositiveSmallIntegerField()
    field_3 = models.PositiveSmallIntegerField()
    field_4 = models.PositiveSmallIntegerField()
    field_5 = models.PositiveSmallIntegerField()
    field_6 = models.PositiveSmallIntegerField()
    field_7 = models.PositiveSmallIntegerField()
    field_8 = models.PositiveSmallIntegerField()
    field_9 = models.PositiveSmallIntegerField()
    field_10 = models.PositiveSmallIntegerField()
    field_11 = models.PositiveSmallIntegerField()
    field_12 = models.PositiveSmallIntegerField()
    field_13 = models.PositiveSmallIntegerField()
    field_14 = models.PositiveSmallIntegerField()
    field_15 = models.PositiveSmallIntegerField()
    field_16 = models.PositiveSmallIntegerField()
    field_17 = models.PositiveSmallIntegerField()
    field_18 = models.PositiveSmallIntegerField()
    field_19 = models.PositiveSmallIntegerField()
    field_20 = models.PositiveSmallIntegerField()
    field_21 = models.PositiveSmallIntegerField()
    field_22 = models.PositiveSmallIntegerField()
    field_23 = models.PositiveSmallIntegerField()
    dcount = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name_q} --> {self.date}'

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'Графики'
        ordering = ['date']
        constraints = [
            models.UniqueConstraint(fields=['name_q', 'date'], name='ДЭЭЭЭЭЭЭ')
        ]



