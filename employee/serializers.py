from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'position',  'chief', 'salary', 'paid_salary']