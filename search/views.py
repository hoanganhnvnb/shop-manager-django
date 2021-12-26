from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from unidecode import unidecode
import re

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

def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s

class GetItemsByTitle(APIView):
    def get(self, request, *args, **kwargs):
        search_text = str(kwargs.get('search_text'))
        search_text_bytes = search_text.encode('utf-8')
        message_bytes = base64.b64decode(search_text_bytes)
        search = message_bytes.decode('utf-8')
        search_text = no_accent_vietnamese(search)
        item_list = Items.objects.filter(title__unaccent__icontains=search_text)
        
        data = ItemsSerializers(item_list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)
    

        
class GetItemsByCompanyName(APIView):
    def get(self, request, *args, **kwargs):
        search_text = str(kwargs.get('search_text'))
        search_text_bytes = search_text.encode('utf-8')
        message_bytes = base64.b64decode(search_text_bytes)
        search = message_bytes.decode('utf-8')
        search_text = no_accent_vietnamese(search)
        item_list = Items.objects.filter(companyName__unaccent__icontains=search_text)
        data = ItemsSerializers(item_list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)
    
class GetItemsByCategoryTitle(APIView):
    
    def get(self, request, *args, **kwargs):
        search_text = str(kwargs.get('search_text'))
        search_text_bytes = search_text.encode('utf-8')
        message_bytes = base64.b64decode(search_text_bytes)
        search = message_bytes.decode('utf-8')
        search_text = no_accent_vietnamese(search)
        item_list = Items.objects.filter(category__title__unaccent__icontains=search_text)
        data = ItemsSerializers(item_list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)