import os
from celery import Celery
from celery import task
from .models import Employee
from django.conf import settings

celery = Celery('tasks', broker='amqp://guest@localhost//')
celery.config_from_object('django.conf:settings')
celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "employee.settings"

@task
def salary_calculation(salary_id):
    salary = Employee.objects.get(id=salary_id)
    new_salary = salary + (salary / 160) * 2
    salary = new_salary
    return salary
