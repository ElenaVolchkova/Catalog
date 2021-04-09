from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    salary = models.FloatField()
    employment_date = models.DateTimeField(blank=True, null=True)
    paid_salary = models.FloatField()
    chief = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name
