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

# This will edit schedule every time, if task not exist.
# If there are need to add task one time -- maybe this is good
# reason to write this tsk in data migration
app.conf.beat_schedule = {
    'Accrue salary to all workers': {
        'task': 'employee.apps.employee.tasks.salary_calculation',
        'schedule': timedelta(hours=2)
    },
}
