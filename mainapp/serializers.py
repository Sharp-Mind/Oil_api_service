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
        date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        liquid = serializers.FloatField()
        oil = serializers.FloatField()
        water = serializers.FloatField()
        wct = serializers.FloatField()