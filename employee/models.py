from django.db import models


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
    )
    name = models.CharField(max_length=200)
    salary = models.FloatField()
    employment_date = models.DateField(null=True, blank=True)
    paid_salary = models.FloatField()
    chief = models.ForeignKey("employee.Employee", on_delete=models.SET_NULL, null=True, blank=True)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name
