from cgitb import reset
from oilapiservice.celery import app
from celery import Celery
from mainapp.models import Reports
from rest_framework.response import Response
from mainapp.kernel import main as run

@app.task
def calculate(request_data):
    output_data = run(**request_data)
      
    # Reports.objects.create(
    #     date=output_data['date'],
    #     liquid=output_data['liquid'],
    #     oil=output_data['oil'],
    #     water=output_data['water'],
    #     wct=output_data['wct'],
    #     task_id = app.id
    # )
    return output_data
   