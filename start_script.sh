#!/bin/bash
source ../venv/bin/activate
pip install requirements.txt
python manage.py runserver
celery -A oilapiservice worker --loglevel=info