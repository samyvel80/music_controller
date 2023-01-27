import json

from .models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

from rest_framework import generics

class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


'''
@api_view(['GET'])
def api_view(request, *args, **kwargs):
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
        #data = model_to_dict(query, fields=('name', 'content', 'price', 'get_discount'))
        serializer = ProductSerializer(query)
        data = serializer.data
        # Response => Serialise les donnees dict-> en Json
    return Response(data)

@api_view(['POST'])
def api_view(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'detail': 'invalid data'})
'''