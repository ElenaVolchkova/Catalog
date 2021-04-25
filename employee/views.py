from django.shortcuts import render
from . import serializers
from .models import Employee
from rest_framework import generics
from django.contrib.auth.models import User



class EmployeeList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class EmployeeDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


def employee_list(request):
    employees = Employee.objects.all()
    context = {"employee_list": employees}
    return render(request, 'employee/employee_list.html', context)
