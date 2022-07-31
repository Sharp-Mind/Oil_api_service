from oilapiservice.celery import app
from mainapp.serializers import ReportsSerializer
from mainapp.models import Reports
from rest_framework.response import Response

@app.task
def calculate(request_data):   
    serializer = ReportsSerializer(data=request_data)
    serializer.is_valid(raise_exception=True)      

    report = Reports.objects.create(
        date = request_data['date'],
        liquid = request_data['liquid'],
        oil = request_data['oil'],
        water = request_data['water'],
        wct = request_data['wct']           
    )
    
    return {'report': ReportsSerializer(report).data}