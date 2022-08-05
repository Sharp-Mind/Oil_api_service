from oilapiservice.celery import app
from celery import Celery
from mainapp.models import Reports
from django_celery_results.models import TaskResult
from mainapp.kernel import main as run


@app.task
def calculate(request_data):

    new_report = Reports.objects.create(
        task=TaskResult.objects.get(task_id=calculate.request.id)
    )

    output_data = run(**request_data)

    data_to_base = output_data.to_dict()
   
    new_report.date = data_to_base["date"]
    new_report.liquid = data_to_base["liquid"]
    new_report.oil = data_to_base["oil"]
    new_report.water = data_to_base["water"]
    new_report.wct = data_to_base["wct"]

    new_report.save()
