from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from items.models import Items
from items.serializers import ItemsSerializers

from django.db import connection
with connection.cursor() as cursor:
    cursor.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm')

from django.db.models import CharField
from django.db.models.functions import Lower
import base64
from django.contrib.postgres.search import TrigramSimilarity

CharField.register_lookup(Lower)

# Create your views here.

class GetItemsByTitle(APIView):
    def get(self, request, *args, **kwargs):
        search_text = kwargs.get('search_text')
        search_text = base64.b64decode(search_text)
        item_list = Items.objects.filter(title__unaccent__icontains=search_text)
        
        data = ItemsSerializers(item_list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)
    

        
class GetItemsByCompanyName(APIView):
    def get(self, request, *args, **kwargs):
        search_text = kwargs.get('search_text')
        search_text = base64.b64decode(search_text)
        item_list = Items.objects.filter(companyName____unaccent__icontains=search_text)
        data = ItemsSerializers(item_list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)
    
class GetItemsByCategoryTitle(APIView):
    
    def get(self, request, *args, **kwargs):
        search_text = kwargs.get('search_text')
        search_text = base64.b64decode(search_text)
        item_list = Items.objects.filter(category__title__unaccent__icontains=search_text)
        data = ItemsSerializers(item_list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)