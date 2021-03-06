from rest_framework import permissions
from rest_framework.permissions import BasePermission


class EmployeePermissions(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


# class HaveAccessAPIPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.has_perm('employee.have_access_api')