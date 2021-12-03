from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from items.models import Items
from items.serializers import ItemsSerializers, ItemsCreateSerializers


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
                'message': 'Create a new Category successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Category unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteItemsView(RetrieveUpdateDestroyAPIView):
    model = Items
    serializer_class = ItemsSerializers

    def put(self, request, *args, **kwargs):
        item = get_object_or_404(Items, id=kwargs.get('pk'))
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
        item = get_object_or_404(Items, id=kwargs.get('pk'))
        item.delete()

        return JsonResponse({
            'message': 'Delete Items successful!'
        }, status=status.HTTP_200_OK)