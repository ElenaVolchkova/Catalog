from django.db import models
from rest_framework import permissions
from django.contrib.auth.models import User


class Employee(models.Model):
    СЕО = 'СЕО'
    MIDDLE = 'MD'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    QA = 'QA'
    POSITION_CHOICES = [
        (СЕО, 'СЕО'),
        (MIDDLE, 'Middle'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (QA, 'QA'),
    ]
    position = models.CharField(
        max_length=20,
        choices=POSITION_CHOICES,
        default=JUNIOR,
        verbose_name='Должность')
    name = models.CharField(max_length=200, verbose_name='ФИО')
    salary = models.FloatField(verbose_name='Зарплата')
    employment_date = models.DateField(null=True, blank=True, verbose_name='Дата приема на работу')
    paid_salary = models.FloatField(verbose_name='Всего выплачено')
    chief = models.ForeignKey("employee.Employee", on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Начальник')
    level = models.IntegerField(default=0, verbose_name='Уровень')
    employee_status = models.BooleanField(default=False, verbose_name='is_staff')


    def __str__(self):
        return self.name

# class EmployeeStatus(models.Model):
#     status = models.BooleanField(default=False, verbose_name='is_staff')

    def get_permissions(self):
        if self.status == False:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]