from urllib import response
from rest_framework import serializers
import oilapiservice.settings as settings

# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from mainapp.models import Reports
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser



    # def create(self, validated_data):
    #     raise NotImplementedError('`create()` must be implemented.')


class ReportsSerializer(serializers.Serializer):
    date_start = serializers.DateField()
    date_fin = serializers.DateField()
    lag =  serializers.IntegerField()
    task_date = serializers.DateField()
    date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    liquid = serializers.CharField()
    oil = serializers.CharField()
    water = serializers.CharField()
    wct = serializers.CharField()
    task_id = serializers.CharField()

class InputSerializer(serializers.Serializer):
    date_start = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    date_fin = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    lag = serializers.IntegerField()

class TasksSerializer(serializers.Serializer):
    date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    task = serializers.CharField()