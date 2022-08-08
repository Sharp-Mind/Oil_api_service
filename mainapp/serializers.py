from dataclasses import field, fields
from rest_framework import serializers
from oilapiservice.settings import DATE_INPUT_FORMATS
from mainapp.models import Calculation, TaskResult


class TaskResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult        
        fields = 'status'


class CalculationResultSerializer(serializers.ModelSerializer):
    cid = serializers.CharField()
    task_created = serializers.DateTimeField()
    task_status = TaskResultSerializer(many=True, read_only=True)
    class Meta:
        model = Calculation
        fields = ['cid', 'task_created', 'task_status']


class SingleCalculationResultSerializer(serializers.ModelSerializer):    
    task_status = TaskResultSerializer(many=True, read_only=True)   
    class Meta:
        model = Calculation
        fields = [
            "cid",
            "task_created",
            "date",
            "liquid",
            "oil",
            "water",
            "wct",
            "task_status",
        ]


class CalculationInputSerializer(serializers.Serializer):
    date_start = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    date_fin = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    lag = serializers.IntegerField()
