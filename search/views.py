from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from items.models import Items
from items.serializers import ItemsSerializers

# Create your views here.

class GetItemsByTitle(APIView):
    def get(self, request, *args, **kwargs):
        name
        search_text = kwargs.get('search_text')
        item_list = Items.objects.filter(title__unaccent__icontains=search_text)
        data = ItemsSerializers(item_list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)
    

        
class GetItemsByCompanyName(APIView):
    def get(self, request, *args, **kwargs):
        search_text = kwargs.get('search_text')
        item_list = Items.objects.filter(companyName__unaccent__icontains=search_text)
        data = ItemsSerializers(item_list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)
    
class GetItemsByCategoryTitle(APIView):
    
    def get(self, request, *args, **kwargs):
        search_text = kwargs.get('search_text')
        item_list = Items.objects.filter(category____unaccent__icontains=search_text)
        data = ItemsSerializers(item_list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)