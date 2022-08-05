"""
Файл настроек Celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oilapiservice.settings")

app = Celery("celery_django")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
