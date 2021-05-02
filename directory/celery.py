import os
from datetime import timedelta
from celery import Celery
from . import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'directory.settings')

app = Celery('employee')

# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'Accrue salary to all workers': {
        'task': 'employee.apps.employee.tasks.salary_calculation',
        'schedule': timedelta(hours=2)
    },
}
