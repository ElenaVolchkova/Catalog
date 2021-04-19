from django.contrib import admin
from .models import Employee
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html


# @admin.site.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'chief', 'salary', 'paid_salary',)
    list_filter = ('position', 'level',)
    actions = ['clean_paid_salary']
    list_display_links = ('name', 'chief',)
    search_fields = ('name',)

    def clean_paid_salary(self, request, queryset):
        queryset.update(paid_salary=0)


admin.site.register(Employee, EmployeeAdmin)
