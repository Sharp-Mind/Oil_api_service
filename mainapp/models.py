from django.db import models
import datetime
from django.utils import timezone

class Reports(models.Model):
    date_start = models.DateField(verbose_name='Input date of start', null=True)
    date_fin = models.DateField(verbose_name='nput date of finish', null=True)
    lag =  models.IntegerField(verbose_name='Lag', null=True)
    task_date = models.DateField(verbose_name='Date of row creation', auto_now_add=True)
    date = models.CharField(verbose_name='Date', max_length=10000, null=True)
    liquid = models.CharField(verbose_name='Liquid', max_length=10000, null=True)
    oil = models.CharField(verbose_name='Oil', max_length=10000, null=True)
    water = models.CharField(verbose_name='Water', max_length=10000)
    wct = models.CharField(verbose_name='wct', max_length=10000, null=True)
    task_id = models.CharField(verbose_name='Task ID', max_length=36, null=True)
    task_state = models.CharField(verbose_name='Task state', max_length=36, null=True)

class Tasks(models.Model):
    date = models.DateField(verbose_name='Date', auto_now_add=True)
    task = models.CharField(verbose_name='Task ID', max_length=36, null=True)

    class Meta:
        ordering = ['date']
        