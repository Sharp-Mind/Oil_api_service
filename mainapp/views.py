from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from mainapp.models import Reports
from django_celery_results.models import TaskResult
from mainapp.serializers import ReportsSerializer, InputSerializer, OneReportSerializer
from celery import Celery
from mainapp.pagination import StandartResultsSetPagination
from mainapp.tasks import calculate
from django.core.exceptions import ObjectDoesNotExist


class ReportsListAPIView(generics.ListAPIView):

    pagination_class = StandartResultsSetPagination
    serializer_class = ReportsSerializer
    queryset = Reports.objects.all()

    def get(self, request, *args, **kwargs):

        if "task_id" in request.data.keys():

            try:
                report = Reports.objects.get(
                    task=TaskResult.objects.get(task_id=request.data["task_id"])
                )
                serializer = OneReportSerializer(report)
                if report.task.status in ("PENDING", "STARTED"):
                    return Response("None")
                return Response(serializer.data)

            except ObjectDoesNotExist:
                return Response("Does not exist")            

        return super().get(request, *args, **kwargs)

    def post(self, request):

        serializer = InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        new_task = calculate.delay(request.data)

        return Response({"task_id": new_task.id})
