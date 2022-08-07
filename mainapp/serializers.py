from rest_framework import serializers
from oilapiservice.settings import DATE_INPUT_FORMATS
from mainapp.models import TaskResult

class CalculationResultSerializer(serializers.Serializer):
    cid = serializers.CharField()
    task_created = serializers.DateTimeField()
    task_status = serializers.CharField(source="TaskResult.objects.get(task_id=cid).status", read_only=True)


class SingleCalculationResultSerializer(serializers.Serializer):
    cid = serializers.CharField()
    task_created = serializers.DateTimeField()
    task_status = serializers.CharField(source="task.status", read_only=True)    
    date = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    liquid = serializers.CharField()
    oil = serializers.CharField()
    water = serializers.CharField()
    wct = serializers.CharField()


class CalculationInputSerializer(serializers.Serializer):
    date_start = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    date_fin = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    lag = serializers.IntegerField()
