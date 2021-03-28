from django.shortcuts import render
from employee.models import Employee

# Create your views here.
def employee_list(request):
	employees = Employee.objects.all()
	context = {"employee_list": employees}
	return render(request, 'employee/employee_list.html', context)
