from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

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
        order_details = OrderDetailsModel.objects.all().order_by('id')
        paginator = PageNumberPagination()
        paginator.page_size = 100
        paginator.max_page_size = 1000
        page = paginator.paginate_queryset(order_details, request)
        serializer = OrderDetailsSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        product = ProductModel.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    