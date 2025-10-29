from django.shortcuts import redirect
from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if (isinstance(exc, NotAuthenticated) or isinstance(exc, PermissionDenied)) and 'text/html' in context['request'].META.get('HTTP_ACCEPT', ''):
        return redirect('/api/login/')

    return response
