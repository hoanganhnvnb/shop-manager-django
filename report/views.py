from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from report.models import Report
from user.models import CustomerUser

from .serializers import ReportSerializer

# Create your views here.

class GetReport(APIView):
    def get(self):
        report = Report.objects.get(pk=1)
        user_list = CustomerUser.objects.all().filter(is_superuser=True)
        report.count_nv = len(user_list)
        report.save()
        data = ReportSerializer(report)
        return Response(data=data.data, status=status.HTTP_200_OK)
