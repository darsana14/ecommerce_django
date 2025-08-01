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


@api_view(['GET'])
def getProduct(request, id):
    product_object = Products.objects.get(id=id)
    serialised_product = ProductSerializers(product_object)
    return Response(serialised_product.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def createProduct(request):
    serialised_product = ProductSerializers(data=request.data)
    if serialised_product.is_valid():
        product = serialised_product.save()
        return Response(product.id, status=status.HTTP_200_OK)
    
    return Response("Invalid Payload")

@api_view(['DELETE'])
def deleteProduct(request, id):
    product_object = Products.objects.get(id=id)
    if product_object is not None:
        product_object.delete()
        return Response("Deleted", status=status.HTTP_200_OK)
    return Response("Not Found", status=status.HTTP_400_BAD_REQUEST)