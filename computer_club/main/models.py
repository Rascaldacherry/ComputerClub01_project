from django.conf import settings
from django.db import models


# Create your models here.
# import datetime

from django.db import models


class AbcModel(models.Model):
    task = models.CharField(
        verbose_name="Формулировка  задачи",
        default="Даны вещественные положительные числа a, b, c, d. Выясните, может ли прямоугольник со сторонами a, b уместиться внутри прямоугольника c, d, так чтобы каждая сторона внутреннего прямоугольника была параллельна или перпендикулярна стороне внешнего прямоугольника.",
        max_length=255,
    )
    a = models.IntegerField(
        verbose_name="Значение А", default=1
    )
    b = models.IntegerField(
        verbose_name="Значение B", default=1
    )
    c = models.IntegerField(
        verbose_name="Значение C", default=1
    )
    d = models.IntegerField(
        verbose_name="Значение D", default=1
    )

    result = models.CharField(
        verbose_name="Результат",
        default="Результат не определен",
        max_length=255,
    )
    current_date = models.DateTimeField(
        verbose_name="Дата изменения(save)", auto_now=True
    )

    def __str__(self):
        # return self.task
        # return '%s %s' % (self.task, self.current_date)
        return f"self.id:{self.id}; self.task:{self.task}"

    class Meta:
        verbose_name = "A_B_C_Таблица"
        verbose_name_plural = "A_B_C_Таблицы"
        ordering = ("-pk", )


# current_date = models.DateTimeField("ДатаВремя", default=datetime.datetime.now())
# current_date = models.DateTimeField("ДатаВремя", auto_now_add=True)

# python manage.py makemigrations
# python manage.py migrate

# admin.py
# from django.contrib import admin
# # Register your models here.
# from .models import Abc
# admin.site.register(Abc)


# forms.py
# from django.forms import ModelForm
# from .models import Abc
#
# class CreateAbcForm(ModelForm):
#     class Meta:
#         model = Abc
#         fields = ['task', 'a' ,'b' ,'c', 'c_calc']