from django.contrib import admin
from .models import Employee


# admin.site.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'chief', 'salary', 'paid_salary')
    list_filter = ('position', 'level')


admin.site.register(Employee, EmployeeAdmin)
