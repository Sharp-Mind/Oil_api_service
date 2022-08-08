from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from mainapp.models import Calculation
from django_celery_results.models import TaskResult
from mainapp.serializers import (
    CalculationResultSerializer,
    CalculationInputSerializer,
    SingleCalculationResultSerializer,
)
from celery import Celery
from mainapp.pagination import StandartResultsSetPagination
from mainapp.tasks import calculate
from django.core.exceptions import ObjectDoesNotExist


class CalculationListAPIView(generics.ListAPIView):

    pagination_class = StandartResultsSetPagination
    serializer_class = CalculationResultSerializer
    queryset = Calculation.objects.all()

    ordering_fields = ["task_created"]
    ordering = ["-task_created"]

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)

    def post(self, request):

        serializer = CalculationInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_task = calculate.delay(request.data)

        return Response({"cid": new_task.id})


class SingleCalculationListAPIView(generics.ListAPIView):

    pagination_class = StandartResultsSetPagination
    serializer_class = CalculationResultSerializer
    queryset = Calculation.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            task_obj = TaskResult.objects.get(task_id=self.kwargs["cid"])
            calculation = self.queryset.get(cid=self.kwargs["cid"])

            if task_obj.status in ("PENDING", "STARTED"):
                return Response({"result": "None"})
            else:

                serializer = SingleCalculationResultSerializer(calculation)

                if "fields" in request.data.keys():
                    optional_fields = dict()

                    if "elapsed_time" in request.data["fields"]:
                        optional_fields["elapsed_time"] = (
                            task_obj.date_done - task_obj.date_created
                        )

                    if "name" in request.data["fields"]:
                        optional_fields["name"] = task_obj.task_name

                    return Response(
                        {"result": serializer.data, "optional": optional_fields}
                    )

                return Response({"result": serializer.data})

        except ObjectDoesNotExist:
            return Response({"result": "Does not exist"})
