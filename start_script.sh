#!/bin/bash
source ../venv/bin/activate
python manage.py runserver
celery -A oilapiservice worker --loglevel=info