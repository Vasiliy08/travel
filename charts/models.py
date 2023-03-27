from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, Q
from django.urls import reverse
from pytils.translit import slugify


#
# □ "null” — поле таблицы не может хранить значение null, т. е. его следует заполнить;
# □ "blank” —в элемент управления должно быть занесено значение;
# □ "invalid" —неверный формат значения;
# □ "invalid choice’’ —в поле со списком заносится значение, не указанное в списке;
# □ "unique" —в поле заносится неуникальное значение, что недопустимо;
# □ "unique for date" — в поле заносится значение, неуникальное в пределах даты,
# что недопустимо;
# □ "invalid date" — значение даты хоть и введено правильно, но некорректное
# (например, 35.14.2020);
# □ "invalid time" — значение времени хоть и введено правильно, но некорректное
# (например, 25:73:80);
# □ "invalid datetime" — значение даты и времени хоть и введено правильно, но
# некорректное (например, 35.14.2020 25:73:80);
# □ "min iength" — длина сохраняемой в поле строки меньше указанного минимума;
# □ "max length" — длина сохраняемой в поле строки больше указанного максимума;
# □ "nuii characters not aiiowed" — сохраняемая строка содержит нулевые символы \хоо;
# Гпава 4. Модели: базовые инструменты_________________________________________ 115
# □ ’’min vaiue” — сохраняемое в поле число меньше указанного минимума;
# □ "max value” — сохраняемое в поле число больше указанного максимума;
# □ "max digits"— общее КОЛИЧеСТВО Цифр В Сохраняемом числе типа Decimal
# больше заданного;
# □ "max decimal places”— количество цифр в дробной части сохраняемого числа
# типа Decimal больше заданного;
# □ "max whole digits" — количество цифр в целой части сохраняемого числа типа
# Decimal больше разности между максимальным общим количеством цифр и количеством цифр в дробной части


class Question(models.Model):
    question_text = models.CharField(max_length=200, error_messages={'invalid': 'sfdfsfsd'})
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
    name_q = models.CharField(max_length=100, verbose_name="Имя", error_messages={'blank': 'sfdfsfsd'})
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

    def get_absolute_url(self):
        return reverse('charts:charts_detail', kwargs={'post_str': self.name_q})

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'Графики'
        ordering = ['date']
        constraints = [
        #     models.UniqueConstraint(fields=['name_q', 'date'], name='ДЭЭЭЭЭЭЭ'),
            models.CheckConstraint(check=models.Q(dcount__gte=0) & models.Q(dcount__lte=24), name='qwEWQ')
        ]


