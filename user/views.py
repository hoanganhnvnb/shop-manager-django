from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

import FCMManager as fcm

from .models import CustomerUser
from .serializers import UserSerializer, UserInformationSerializer, SimpleUserSerializer, UpdateLocalTokenUserSerializer


# Create your views here.

class UserRegisterAPIView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()

            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'error_message': 'This user has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)


class UserInformationAPIView(APIView):

    def get(self, request):
        
        fcm.sendPush("Get Info", "Push from django ahihihihi", ["flvYvodQRfqZPq0_8A3CWl:APA91bH5WtuJZaQZIfdbYcTeFfknlhejtKj_a-ohLIds5whKSo4LF6wNVQ4S0hvUV3AoEPJOF3JDbC05xBM6sbx-bbImOQccvwx9_bDzgwSDTiykln7JzjCA4tbU1oWfHl9bxe5MeZig"])
        
        if request.user.is_authenticated:
            user = request.user
        else:
            return JsonResponse({
                'message': 'Not Authenticated!'
            }, status=status.HTTP_400_BAD_REQUEST)
        data = SimpleUserSerializer(user)
        return Response(data=data.data, status=status.HTTP_200_OK)

class ListCreateUserAPIView(ListCreateAPIView):
    model = CustomerUser
    serializer_class = UserInformationSerializer

    def get_queryset(self):
        return CustomerUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserInformationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()

            return JsonResponse({
                'message': 'Create a new User successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new User unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    model = CustomerUser
    serializer_class = UserInformationSerializer

    def put(self, request, *args, **kwargs):
        user = get_object_or_404(CustomerUser, id=kwargs.get('pk'))
        serializer = UserInformationSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update User successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update User unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(CustomerUser, id=kwargs.get('pk'))
        user.delete()

        return JsonResponse({
            'message': 'Delete User successful!'
        }, status=status.HTTP_200_OK)
        
class UpdateTokenUserView(RetrieveUpdateDestroyAPIView):
    model = CustomerUser
    serializer_class = UpdateLocalTokenUserSerializer

    def put(self, request, *args, **kwargs):
        user = get_object_or_404(CustomerUser, id=kwargs.get('pk'))
        serializer = UpdateLocalTokenUserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            data = SimpleUserSerializer(data=user)
            return Response(data=data.data, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update new Token unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)