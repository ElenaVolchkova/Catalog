from django.conf import settings
from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    salary = models.FloatField()
    employment_date = models.DateTimeField(blank=True, null=True)
    information_about_the_paid_salary = models.FloatField()


    def __str__(self):
        return self.name