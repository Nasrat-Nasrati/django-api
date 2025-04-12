from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from reporting.models import Orders
from reporting.serializers import OrdersSerializer


# Create your views here.

class ReportingViewSet(APIView):
    def get(self,request):
        answer={'id':'43','name':'Question'}
        return Response(answer)


class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrdersSerializer
    def get_queryset(self):
        return Orders.objects.all().order_by('-created_time')
    
    
        