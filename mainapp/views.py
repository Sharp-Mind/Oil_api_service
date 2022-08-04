from multiprocessing.pool import AsyncResult
from mainapp import serializers
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from mainapp.models import Reports, Tasks
from mainapp.serializers import ReportsSerializer, InputSerializer
from mainapp.tasks import calculate
from celery import Celery
from celery.result import AsyncResult as ar
from oilapiservice.celery import app
from rest_framework.pagination import PageNumberPagination
from mainapp.pagination import StandartResultsSetPagination
import pandas as pd
import json

class ReportsListAPIView(generics.ListAPIView):
    
  
    pagination_class = StandartResultsSetPagination
    serializer_class = ReportsSerializer      
    queryset = Reports.objects.all()  
    

    def get(self, request, *args, **kwargs):
        # if 'task_id' in request.data.keys():            
        #     print(AsyncResult(request.data['task_id'], app=app).get())                
        return super().get(request, *args, **kwargs)

    
    def post(self, request):
        serializer = InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_task = calculate.delay(request.data)
        res = ar(new_task.id)
        print(res.status)
                
        return Response({'status': 'Task added', 'id': new_task.id})
