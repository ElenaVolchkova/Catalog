from django.shortcuts import render
from . import serializers
from .models import Employee
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [DjangoFilterBackend]


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['level']


class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


def employee_list(request):
    employees = Employee.objects.all()
    context = {"employee_list": employees}
    return render(request, 'employee/employee_list.html', context)
