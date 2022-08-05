from django.db import models
from django_celery_results.models import TaskResult

class Reports(models.Model):    
    date = models.CharField(verbose_name="Date", max_length=10000, null=True)
    liquid = models.CharField(verbose_name="Liquid", max_length=10000, null=True)
    oil = models.CharField(verbose_name="Oil", max_length=10000, null=True)
    water = models.CharField(verbose_name="Water", max_length=10000)
    wct = models.CharField(verbose_name="wct", max_length=10000, null=True)    
    task = models.ForeignKey(TaskResult, on_delete=models.CASCADE, null=True)
