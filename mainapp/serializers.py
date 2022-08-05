from rest_framework import serializers
from oilapiservice.settings import DATE_INPUT_FORMATS

class ReportsSerializer(serializers.Serializer):
    task_id = serializers.CharField(source="task.task_id", read_only=True)
    task_created = serializers.CharField(source="task.date_created", read_only=True)
    task_status = serializers.CharField(source="task.status", read_only=True)


class OneReportSerializer(serializers.Serializer):
    task_id = serializers.CharField(source="task.task_id", read_only=True)
    task_created = serializers.CharField(source="task.date_created", read_only=True)
    task_status = serializers.CharField(source="task.status", read_only=True)    
    date = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    liquid = serializers.CharField()
    oil = serializers.CharField()
    water = serializers.CharField()
    wct = serializers.CharField()


class InputSerializer(serializers.Serializer):
    date_start = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    date_fin = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    lag = serializers.IntegerField()
