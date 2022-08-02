from django.db import models
import datetime
from django.utils import timezone

class Reports(models.Model):
    task_date = models.DateField(verbose_name='Date of raw creation', auto_now_add=True, null=True)
    date = models.CharField(verbose_name='Date', max_length=10000)
    liquid = models.CharField(verbose_name='Liquid', max_length=10000)
    oil = models.CharField(verbose_name='Oil', max_length=10000)
    water = models.CharField(verbose_name='Water', max_length=10000)
    wct = models.CharField(verbose_name='wct', max_length=10000)
    task_id = models.CharField(verbose_name='Task ID', max_length=36, null=True)

class Tasks(models.Model):
    date = models.DateField(verbose_name='Date', auto_now_add=True)
    task = models.CharField(verbose_name='Task ID', max_length=36, null=True)

    class Meta:
        ordering = ['date']
        