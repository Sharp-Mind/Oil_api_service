from rest_framework.views import APIView
from rest_framework.response import Response
from mainapp.models import Reports
from mainapp.serializers import ReportsSerializer
from mainapp.tasks import calculate
from celery import Celery
from oilapiservice.celery import app
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt



# class ReportsAPIView(APIView):
#     def get(self, request):
#         queryset = Reports.objects.all()
#         return Response({'reports': ReportsSerializer(queryset, many=True).data})   

#     def post(self, request):
#         # calulate(request)
#         pass

# def task(request):
#     if request.method == 'POST':        
#         calculate(request)

@csrf_exempt        
@api_view(['GET', 'POST'])
def report_info(request):
    if request.method == 'GET':
        queryset = Reports.objects.all()
        return Response({'reports': ReportsSerializer(queryset, many=True).data})
    elif request.method == 'POST':
        task = calculate.delay(request.data)
        print(task)      
        return Response(task.result)

