from ast import While
from urllib import request
from mainapp.models import Reports
from mainapp.serializers import ReportsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import queue
import asyncio


objs_queue = queue.Queue()
posting = False


class ReportsAPIView(APIView):
    def get(self, request):
        queryset = Reports.objects.all()
        return Response({'reports': ReportsSerializer(queryset, many=True).data})

    # def post(self, request):

    async def to_queue(self, request):                        
        objs_queue.put(request)
        # if not posting:
        #     self.do_post()
    
    async def to_post(self, objs_queue):
        # self.to_queue(request)
        posting = True
        while objs_queue:           
            request = objs_queue.get()
            serializer = ReportsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)        

            report = Reports.objects.create(
                date = request.data['date'],
                liquid = request.data['liquid'],
                oil = request.data['oil'],
                water = request.data['water'],
                wct = request.data['wct']            
            )       
            result = {'report': ReportsSerializer(report).data}    
            # return Response({'report': ReportsSerializer(report).data})
        posting = False


    async def post(self, request) -> Response:
        loop = asyncio.get_event_loop()               
        loop.create_task(self.to_queue(request))
        loop.create_task(self.to_post(request))
        result = await self.to_post()
        if result:        
            return Response(result)
            result = None



# async def async_view(request):
#     loop = asyncio.get_event_loop()
#     loop.create_task(http_call_async())
#     return HttpResponse("Non-blocking HTTP request")
    
        