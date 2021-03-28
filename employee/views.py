from django.shortcuts import render

# Create your views here.
def employee_list(request):
    return render(request, 'employee/employee_list.html', {})