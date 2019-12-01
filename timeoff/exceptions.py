from django.http import JsonResponse
from rest_framework import status


def not_found(request, *args, **kwargs):
    """
    Generic 404 error handler.
    """
    data = {
        'error': 'Not Found (404)'
    }
    return JsonResponse(data, content_type="application/json", status=status.HTTP_404_NOT_FOUND)
