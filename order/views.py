from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from cart.models import Cart, CartItems
from items.models import Items
from order.models import Order
from order.serializer import OrderSerializer, OrderSimpleSerializer, OrderPaidSerializer


class ListCreateOrderAPIView(ListCreateAPIView):
    model = Order
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = OrderSimpleSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            cart = serializer.validated_data.get('cart')

            cart_items = CartItems.objects.filter(cart=cart)
            order_total = 0
            for cart_item in cart_items:
                total_price_item = cart_item.items.sellPrice * cart_item.quantity
                order_total = order_total + total_price_item

            serializer.validated_data['order_total'] = order_total

            serializer.save()

            return JsonResponse({
                'message': 'Create a new Order successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Order unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteOrderView(RetrieveUpdateDestroyAPIView):
    model = Order
    serializer_class = OrderSerializer

    def put(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs.get('pk'))
        serializer = OrderSerializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Order successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Items unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs.get('pk'))
        order.delete()

        return JsonResponse({
            'message': 'Delete Items successful!'
        }, status=status.HTTP_200_OK)


class UpdateTotalOrderAPIView(APIView):

    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs.get('pk'))
        serializer = OrderSerializer(order, data=request.data)
        cart_items = CartItems.objects.filter(cart=order.cart)
        order_total = 0
        for cart_item in cart_items:
            total_price_item = cart_item.items.sellPrice * cart_item.quantity
            order_total = order_total + total_price_item
        order.order_total = order_total
        order.save()

        return JsonResponse({
            'message': 'update order total price Items successful!'
        }, status=status.HTTP_200_OK)
        
class OrderPaidAPIView(RetrieveUpdateDestroyAPIView):
    model = Order
    serializer_class = OrderPaidSerializer
    
    def put(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs.get('pk'))
        serializer = OrderPaidSerializer(order, data=request.data)

        if serializer.is_valid():
            if not order.is_completed:
                order.is_completed = True
                cart_items = CartItems.objects.filter(cart=order.cart)
                
                order_total = 0
                if cart_items:
                    for cart_item in cart_items:
                        item = Items.objects.get(pk=cart_item.items)
                        quantity_to_buy = cart_item.quantity
                        
                        total_price_item = item.sellPrice * quantity_to_buy
                        order_total = order_total + total_price_item
                        
                        item.quantity = item.quantity - quantity_to_buy
                        item.quantity_sold = item.quantity_sold + quantity_to_buy
                        item.save()
                    order.order_total = order_total
                    order.save()
                else:
                    return JsonResponse({
                        'message': 'Paid Order: Cart is empty!'
                    }, status=status.HTTP_400_BAD_REQUEST)
                    

            return JsonResponse({
                'message': 'Paid Order successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Paid Items unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)
    
        