from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'user', 'cart', 'description', 'is_completed', 'order_total')

class OrderSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'user', 'cart', 'description', 'is_completed', 'order_total', 'create_at')
        
class OrderPaidSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ('is_completed', )