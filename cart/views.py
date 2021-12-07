from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart, CartItems
from cart.serializers import CartSerializers, CartCreateSerializers, CartItemsSerializers
from items.models import Items


class ListCreateCartAPIView(ListCreateAPIView):
    model = Cart
    serializer_class = CartSerializers

    def get_queryset(self):
        return Cart.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = CartCreateSerializers(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user']
            try:
                have_active_cart = True
                cart_queryset = Cart.objects.filter(user=user_id)
                active_cart = cart_queryset.get(active=True)
            except Cart.DoesNotExist:
                have_active_cart = False
            if have_active_cart:
                active_cart.active = False
                active_cart.save()
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Cart successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Cart unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteCartView(RetrieveUpdateDestroyAPIView):
    model = Cart
    serializer_class = CartSerializers

    def put(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, id=kwargs.get('pk'))
        serializer = CartCreateSerializers(cart, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Cart successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Cart unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, id=kwargs.get('pk'))
        cart.delete()

        return JsonResponse({
            'message': 'Delete Cart successful!'
        }, status=status.HTTP_200_OK)


class ActiveCartAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        cart_queryset = Cart.objects.filter(user=user_id)
        cart_active = cart_queryset.get(active=True)
        data = CartSerializers(cart_active)
        return Response(data=data.data, status=status.HTTP_200_OK)


# CartItems
class ListCreateCartItemsAPIView(ListCreateAPIView):
    model = CartItems
    serializer_class = CartItemsSerializers

    def get_queryset(self):
        return CartItems.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = CartItemsSerializers(data=request.data)

        if serializer.is_valid():
            cart = serializer.validated_data.get('cart')
            item = serializer.validated_data.get('items')
            item_quantity = serializer.validated_data['quantity']

            if not cart.active:
                return JsonResponse({
                    'message': 'Cart NOT ACTIVE'
                }, status=status.HTTP_400_BAD_REQUEST)

            if item_quantity <= item.quantity:
                cart_item = CartItems.objects.filter(cart=cart, items=item)

                if cart_item:
                    cart_item = cart_item.first()
                    cart_item.quantity = cart_item.quantity + item_quantity
                    item.quantity = item.quantity - item_quantity
                    item.save()
                    cart_item.save()
                else:
                    item.quantity = item.quantity - item_quantity
                    item.save()
                    serializer.save()
            else:
                return JsonResponse({
                    'message': 'The quantity of items is NOT ENOUGH!'
                }, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse({
                'message': 'Create a new CartItems successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new CartItems unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteCartItemsView(RetrieveUpdateDestroyAPIView):
    model = CartItems
    serializer_class = CartItemsSerializers

    def put(self, request, *args, **kwargs):
        cart_items = get_object_or_404(CartItems, id=kwargs.get('pk'))
        serializer = CartItemsSerializers(cart_items, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update CartItems successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update CartItems unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        cart_items = get_object_or_404(CartItems, id=kwargs.get('pk'))
        cart_items.delete()

        return JsonResponse({
            'message': 'Delete CartItems successful!'
        }, status=status.HTTP_200_OK)
