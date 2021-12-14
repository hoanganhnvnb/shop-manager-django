from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from items.models import Items
from items.serializers import ItemsSerializers, ItemsCreateSerializers, ItemsAddQuantitySerializer, ItemsImageSerializer


class ListCreateItemsAPIView(ListCreateAPIView):
    model = Items
    serializer_class = ItemsSerializers

    def get_queryset(self):
        return Items.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ItemsCreateSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Items successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Items unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteItemsView(RetrieveUpdateDestroyAPIView):
    model = Items
    serializer_class = ItemsSerializers

    def put(self, request, *args, **kwargs):
        item = get_object_or_404(Items, barcode=kwargs.get('barcode'))
        serializer = ItemsCreateSerializers(item, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Items successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Items unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        item = get_object_or_404(Items, barcode=kwargs.get('barcode'))
        item.delete()

        return JsonResponse({
            'message': 'Delete Items successful!'
        }, status=status.HTTP_200_OK)


class AddQuantityItemsView(RetrieveUpdateDestroyAPIView):
    model = Items
    serializer_class = ItemsAddQuantitySerializer

    def put(self, request, *args, **kwargs):
        item = get_object_or_404(Items, barcode=kwargs.get('barcode'))
        serializer = ItemsAddQuantitySerializer(item, data=request.data)

        if serializer.is_valid():
            quantity_add = serializer.validated_data.get('quantity')
            item.quantity = item.quantity + quantity_add
            item.save()

            return JsonResponse({
                'message': 'Add Quantity of Items successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Add Quantity of Items unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class AddImageItemsView(RetrieveUpdateDestroyAPIView):
    model = Items
    serializer_class = ItemsImageSerializer

    def put(self, request, *args, **kwargs):
        item = get_object_or_404(Items, barcode=kwargs.get('barcode'))
        serializer = ItemsImageSerializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Add Image of Items successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Add Image of Items unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)
        
class GetItemAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        item = Items.objects.get(barcode=kwargs.get('barcode'))
        data = ItemsSerializers(item)
        return Response(data=data.data, status=status.HTTP_200_OK)
    
class ListPopularItemsAPIView(ListCreateAPIView):
    model = Items
    serializer_class = ItemsSerializers

    def get_queryset(self):
        item_queryset = Items.objects.all().order_by('-quantity_sold')[:10]
        
        return item_queryset