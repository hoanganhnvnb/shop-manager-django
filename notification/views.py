from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from notification.models import Notification
from notification.serializers import NotificationSerializers, NotificationReadSerializers


class ListCreateNotificationAPIView(ListCreateAPIView):
    model = Notification
    serializer_class = NotificationSerializers

    def get_queryset(self):
        return Notification.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = NotificationSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Notification successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Notification unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteNotificationView(RetrieveUpdateDestroyAPIView):
    model = Notification
    serializer_class = NotificationSerializers
    
    def get_queryset(self):
        return Notification.objects.all()
        

    def put(self, request, *args, **kwargs):
        category = get_object_or_404(Notification, id=kwargs.get('pk'))
        serializer = NotificationSerializers(category, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Notification successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Notification unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        category = get_object_or_404(Notification, id=kwargs.get('pk'))
        category.delete()

        return JsonResponse({
            'message': 'Delete Notification successful!'
        }, status=status.HTTP_200_OK)


class UpdateReadNotificationView(RetrieveUpdateDestroyAPIView):
    model = Notification
    serializer_class = NotificationReadSerializers

    def put(self, request, *args, **kwargs):
        noti = get_object_or_404(Notification, id=kwargs.get('pk'))
        serializer = NotificationReadSerializers(noti, data=request.data)

        if serializer.is_valid():
            serializer.save()

            noti.is_read = True;
            noti.save()
            
            return JsonResponse({
                'message': 'Update Notification successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Notification unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class GetNotiByUserSerializer(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
        else:
            return JsonResponse({
                'message': 'Not Authenticated!'
            }, status=status.HTTP_401_UNAUTHORIZED)

        list_noti = Notification.objects.all().filter(user=user).order_by('-id')
        data = NotificationSerializers(list_noti, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


