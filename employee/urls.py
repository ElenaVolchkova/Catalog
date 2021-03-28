from django.urls import path
from employee import views


urlpatterns = [
    path('', views.employee_list, name='employee_list'),
]