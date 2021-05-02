from django.contrib import admin
from .models import Employee
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth.models import User
from rest_framework import permissions


# @admin.site.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'link_to_chief', 'salary', 'paid_salary')
    list_filter = ('position', 'level',)
    actions = ['clean_paid_salary']
    list_display_links = ('name', 'link_to_chief',)
    search_fields = ('name',)

    async def clean_paid_salary(self, request, queryset):
        queryset.update(paid_salary=0)
        if len(queryset) > 20:
            await queryset.update(paid_salary=0)

    def link_to_chief(self, obj):
        link = reverse("admin:employee_employee_change", args=[obj.chief.id]) if obj.chief else "#"
        chief_name = obj.chief.name if obj.chief else "Не задан"
        return format_html('<a href="{}">Начальник</a>', link, chief_name)


# class EmployeePermissions(Employee):
#     permissions = [('have_access_api', 'Have access API')]


admin.site.register(Employee, EmployeeAdmin)
