from oilapiservice.celery import app
from celery import Celery
from mainapp.models import Calculation
from django_celery_results.models import TaskResult
from mainapp.kernel import main as run


@app.task
def calculate(request_data):

    new_calc = Calculation.objects.create(        
        cid = calculate.request.id
    )

    output_data = run(**request_data)

    data_to_base = output_data.to_dict()
   
    new_calc.date = data_to_base["date"]
    new_calc.liquid = data_to_base["liquid"]
    new_calc.oil = data_to_base["oil"]
    new_calc.water = data_to_base["water"]
    new_calc.wct = data_to_base["wct"]

    new_calc.save()
