from dataclasses import field, fields
from rest_framework import serializers
from oilapiservice.settings import DATE_INPUT_FORMATS
from mainapp.models import Calculation, TaskResult


class TaskResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = "status"


class CalculationResultSerializer(serializers.ModelSerializer):
    cid = serializers.CharField()
    task_created = serializers.DateTimeField()

    class Meta:
        model = Calculation
        fields = ["cid", "task_created"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["task_status"] = TaskResult.objects.get(task_id=representation["cid"]).status

        return representation


class SingleCalculationResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculation
        fields = ["cid", "task_created", "date", "liquid", "oil", "water", "wct"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["task_status"] = TaskResult.objects.get(task_id=representation["cid"]).status

        return representation


class CalculationInputSerializer(serializers.Serializer):
    date_start = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    date_fin = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    lag = serializers.IntegerField()
