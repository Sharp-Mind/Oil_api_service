"""
Файл настроек Celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
from __future__ import absolute_import
import os
from celery import Celery

# этот код скопирован с manage.py
# он установит модуль настроек по умолчанию Django для приложения 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oilapiservice.settings')

# здесь вы меняете имя
app = Celery("oilapiservice")

# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# загрузка tasks.py в приложение django
app.autodiscover_tasks()


@app.task
def calulate(x, y):
    serializer = ReportsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)        

    report = Reports.objects.create(
        date = request.data['date'],
        liquid = request.data['liquid'],
        oil = request.data['oil'],
        water = request.data['water'],
        wct = request.data['wct']            
    )       
    # return x / y