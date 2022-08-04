from urllib import response
from rest_framework import serializers
import oilapiservice.settings as settings
from mainapp.models import Reports
from django_celery_results.models import TaskResult
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser


class ReportsSerializer(serializers.Serializer):
    task_id = serializers.CharField(source='task.task_id', read_only=True)
    task_status = serializers.CharField(source='task.status', read_only=True)
    date_start = serializers.DateField()
    date_fin = serializers.DateField()
    lag =  serializers.IntegerField()    
    date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    liquid = serializers.CharField()
    oil = serializers.CharField()
    water = serializers.CharField()
    wct = serializers.CharField()
    
    class Meta:
        model = Reports
        fields = ('task_id')

class InputSerializer(serializers.Serializer):
    date_start = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    date_fin = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    lag = serializers.IntegerField()
