from operator import mod
from django.db import models

class Reports(models.Model):
    date = models.DateField(verbose_name='Date')
    liquid = models.FloatField(verbose_name='Liquid')
    oil = models.FloatField(verbose_name='Oil')
    water = models.FloatField(verbose_name='Water')
    wct = models.FloatField(verbose_name='wct')

    class Meta:
        ordering = ['date']
        