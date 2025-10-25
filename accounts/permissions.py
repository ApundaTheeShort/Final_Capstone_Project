from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admin users to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin' and request.user.is_authenticated


class IsCustodianOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow custodian or admin users to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and (request.user.role == 'custodian' or request.user.role == 'admin')
        # return request.user and request.user.role in ['custodian', 'admin'] and request.user.is_authenticated


class IsCustodian(permissions.BasePermission):
    """
    Custom permission to only allow custodian users to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == 'custodian' and request.user.is_authenticated


class IsStudent(permissions.BasePermission):
    """
    Custom permission to only allow student users to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == 'student' and request.user.is_authenticated
