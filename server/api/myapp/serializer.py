from rest_framework import serializers
from .models import customers,orders,order_details,products


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customers
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_details
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'
        