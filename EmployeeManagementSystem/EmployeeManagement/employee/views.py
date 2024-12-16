from django.shortcuts import render
from rest_framework import views, viewsets
from .models.employee import Employee
from .serializers import EmployeeSerializer


# Create your views here.

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
