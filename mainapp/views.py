from mainapp.models import Reports
from mainapp.serializers import ReportsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ReportsAPIView(APIView):
    def get(self, request):
        queryset = Reports.objects.all()
        return Response({'reports': ReportsSerializer(queryset, many=True).data})

    def post(self, request):
        serializer = ReportsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)        

        report = Reports.objects.create(
            date = request.data['date'],
            liquid = request.data['liquid'],
            oil = request.data['oil'],
            water = request.data['water'],
            wct = request.data['wct']            
        )
        return Response({'report': ReportsSerializer(report).data})