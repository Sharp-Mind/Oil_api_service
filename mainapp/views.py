from multiprocessing.pool import AsyncResult
from mainapp import serializers
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from mainapp.models import Reports  # Tasks
from mainapp.serializers import TasksSerializer, InputSerializer
from mainapp.tasks import calculate
from celery import Celery
from celery.result import AsyncResult
from oilapiservice.celery import app
from rest_framework.pagination import PageNumberPagination
from mainapp.pagination import StandartResultsSetPagination

class ReportsListAPIView(generics.ListAPIView):
    
    # all_tasks = Tasks.objects.all()
    # ten_calculates = None
    pagination_class = StandartResultsSetPagination
    serializer_class = TasksSerializer       
    queryset = None

    # for obj in all_tasks:
    #     Reports.objects.get_or_create(
    #         task_id = obj.task,
    #         task_date = obj.date,
    #         liquid = AsyncResult(obj.task, app=app).get()['liquid'],
    #         oil = AsyncResult(obj.task, app=app).get()['oil'],
    #         water = AsyncResult(obj.task, app=app).get()['water'],
    #         wct = AsyncResult(obj.task, app=app).get()['wct']
    #     )
        # queryset['task_id'] = obj.task
        # queryset['data'] = AsyncResult(obj.task, app=app).get()
    queryset = Reports.objects.all

    def get(self, request, *args, **kwargs):
        if 'task_id' in request.data.keys():            
            print(AsyncResult(request.data['task_id'], app=app).get())
                
        return super().get(request, *args, **kwargs)

    
    def post(self, request):
        serializer = InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_task = calculate.delay(request.data)

        # Tasks.objects.create(
        #     task = new_task.id
        # )
        # print(task.get())
        # print(AsyncResult('e0dab963-6139-4463-bd1f-04293ed454e6', app=app).get())           
        return Response({'status': 'Task added', 'id': new_task.id})
