from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import customers as CustomerModel, orders as OrderModel, order_details as OrderDetailsModel, products as ProductModel
from .serializer import CustomerSerializer,OrderSerializer,OrderDetailsSerializer,ProductSerializer 



@api_view(['GET'])
def customers(request):
    if request.method == 'GET':
        customer = CustomerModel.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    
@api_view(['GET'])
def orders(request):
    if request.method == 'GET':
        order = OrderModel.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def order_details(request):
    if request.method == 'GET':
        order_detail = OrderDetailsModel.objects.all()
        serializer = OrderDetailsSerializer(order_detail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        product = ProductModel.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    