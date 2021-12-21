from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from cart.models import Cart, CartItems
from items.models import Items
from notification.models import Notification
from order.models import Order
from order.serializer import OrderSerializer, OrderSimpleSerializer, OrderPaidSerializer
from user.models import CustomerUser
import FCMManager as fcm


class ListCreateOrderAPIView(ListCreateAPIView):
    model = Order
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = OrderSimpleSerializer(data=request.data)

        if serializer.is_valid():
            if request.user.is_authenticated:
                user = request.user
            else:
                return JsonResponse({
                    'message': 'Not Authenticated!'
                }, status=status.HTTP_400_BAD_REQUEST)
            cart = serializer.validated_data.get('cart')

            cart_items = CartItems.objects.filter(cart=cart)
            order_total = 0
            for cart_item in cart_items:
                total_price_item = cart_item.items.sellPrice * cart_item.quantity
                order_total = order_total + total_price_item

            serializer.validated_data['order_total'] = order_total

            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

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
        if request.user.is_authenticated:
            user_paid = request.user
        else:
            return JsonResponse({
                'message': 'Not Authenticated!'
            }, status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            if not order.is_completed:
                order.is_completed = True
                cart_items = CartItems.objects.filter(cart=order.cart)
                
                order_total = 0
                if cart_items:
                    for cart_item in cart_items:
                        item = Items.objects.get(pk=cart_item.items.id)
                        quantity_to_buy = cart_item.quantity
                        
                        total_price_item = item.sellPrice * quantity_to_buy
                        order_total = order_total + total_price_item
                        
                        item.quantity = item.quantity - quantity_to_buy
                        item.quantity_sold = item.quantity_sold + quantity_to_buy
                        item.save()
                    order.order_total = order_total
                    order.save()
                    order.cart.active = False
                    order.cart.save()
                else:
                    return JsonResponse({
                        'message': 'Paid Order: Cart is empty!'
                    }, status=status.HTTP_400_BAD_REQUEST)

                list_customerUser = CustomerUser.objects.all().filter(is_superuser=True)

                for user in list_customerUser:
                    token = list()
                    title_noti = "User " + user_paid.username + "đã thanh toán!"
                    content_noti = "User " + user_paid.username + "đã thanh toán thành công hóa đơn " + str(order.id)
                    noti = Notification(title=title_noti, content=content_noti, user=user)
                    noti.save()
                    if len(user.token) > 10:
                        token.append(user.token)
                        fcm.sendPush(title=title_noti, msg=content_noti, registration_token=token)

                t_cus = "Bạn đã thanh toán thành công"
                c_cus = "Bạn đã thanh toán thành công hóa đơn: " + str(order.id) + " trị giá: " + str(order.order_total)
                noti_cus = Notification(title=t_cus, content=c_cus, user=user_paid)
                noti_cus.save()
                if len(user_paid.token) > 10:
                    fcm.sendPush(title=t_cus, msg=c_cus, registration_token=list(user_paid.token))

                    

            return JsonResponse({
                'message': 'Paid Order successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Paid Items unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)
        
class GetOrderCompleteByUser(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user_paid = request.user
        else:
            return JsonResponse({
                'message': 'Not Authenticated!'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        order_list = Order.objects.all().filter(user=user_paid, is_completed=True)
        data = OrderSimpleSerializer(order_list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)
    
class GetOrderById(APIView):
    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs.get('pk'))
        data = OrderSimpleSerializer(order)
        return Response(data=data.data, status=status.HTTP_200_OK)
        
    
        