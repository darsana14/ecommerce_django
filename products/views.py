from django.shortcuts import render
from django.http import  HttpResponse
from rest_framework.response import Response
from rest_framework import status


from .serializers import ProductSerializers
from .models import Products
from rest_framework.decorators import api_view


# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")


@api_view(['GET'])
def getProducts(request):
    product_object = Products.objects.all()
    serialised_products = ProductSerializers(product_object, many = True)
    return Response(serialised_products.data, status=status.HTTP_200_OK)