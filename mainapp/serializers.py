from dataclasses import field, fields
from rest_framework import serializers
from oilapiservice.settings import DATE_INPUT_FORMATS
from mainapp.models import Calculation, TaskResult

class TaskResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        # fields = ('id', 'status')
        fields = '__all__'

class CalculationResultSerializer(serializers.Serializer):
    cid = serializers.CharField()
    task_created = serializers.DateTimeField()
    task_status = serializers.CharField(source="TaskResult.objects.get(task_id=cid).status", read_only=True)


class SingleCalculationResultSerializer(serializers.ModelSerializer):
    # cid = serializers.CharField()
    # task_created = serializers.DateTimeField()
    task_status = TaskResultSerializer(many=True, read_only=True)    
    # date = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    # elapsed_time = serializers.DateTimeField()
    # liquid = serializers.CharField()
    # oil = serializers.CharField()
    # water = serializers.CharField()
    # wct = serializers.CharField()
    class Meta:
        model = Calculation
        fields = [
            'cid', 
            'task_created',  
            'date', 
            'liquid', 
            'oil', 
            'water',
            'wct',
            'task_status'
        ]

class CalculationInputSerializer(serializers.Serializer):
    date_start = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    date_fin = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    lag = serializers.IntegerField()
