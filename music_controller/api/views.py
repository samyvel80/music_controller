from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import RoomSerializers
from .models import Room
import json
# Create your views here.
#generics.CreateAPIView)


#GET Room List

def api_view(request, *args, **kwargs):
    # request => instance Httprequest
    print (request.body) #byte string

    data = json.loads(request.body)
    pre_data = json.dumps(data)
    #print(data)
    data['headers'] = dict(request.headers)
    #print(dict(request.GET))
    data['params'] = (request.GET)
    data['post-data'] = request.POST
    print(request.headers)
    data['Content_type'] = request.content_type
    return JsonResponse(data)


class RoomView(APIView):

    def get(self,*args,**kwargs):
        queryset = Room.objects.all()
        serializer = RoomSerializers(queryset, many=True)
        return Response(serializer.data)


#class RoomView(generics.ListAPIView):
class RoomViewset(ReadOnlyModelViewSet):

    serializer_class = RoomSerializers

    def get_queryset(self):
        return Room.objects.all()

class RoomViewCreate(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers