from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from category.models import Category
from category.serializers import CategorySerializers, CategoryCreateSerializers


class ListCreateCategoryAPIView(ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializers

    def get_queryset(self):
        return Category.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = CategoryCreateSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Category successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Category unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteCategoryView(RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerializers

    def put(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs.get('pk'))
        serializer = CategoryCreateSerializers(category, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Category successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Category unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs.get('pk'))
        category.delete()

        return JsonResponse({
            'message': 'Delete Category successful!'
        }, status=status.HTTP_200_OK)
