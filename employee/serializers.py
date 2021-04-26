from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        # owner = serializers.CharField(source='owner.username', read_only=True)
        model = User
        fields = ['id', 'username']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'employment_date', 'position', 'chief', 'salary', 'paid_salary', 'level')
