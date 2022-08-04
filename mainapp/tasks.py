from cgitb import reset
# from multiprocessing.pool import AsyncResult
from oilapiservice.celery import app
from celery import Celery
from mainapp.models import Reports
from mainapp.kernel import main as run
import pandas as pd
from celery.result import AsyncResult

@app.task
def calculate(request_data):
    new_report = Reports.objects.create(
        task_id = calculate.request.id,
        task_state = app.AsyncResult(calculate.request.id).state
        )

    output_data = run(**request_data)
    task_result = AsyncResult(calculate.request.id)        
    data_to_base = output_data.to_dict()    

    new_report.date_fin = request_data['date_fin']
    new_report.date_start = request_data['date_start']
    new_report.lag = request_data['lag']

    new_report.date = data_to_base['date']
    new_report.liquid = data_to_base['liquid']
    new_report.oil = data_to_base['oil']
    new_report.water = data_to_base['water']
    new_report.wct = data_to_base['wct']

    new_report.task_state = task_result.status
    
    new_report.save()

    # def after_return():
    #     new_report.task_state = calculate.AsyncResult(calculate.request.id).state
