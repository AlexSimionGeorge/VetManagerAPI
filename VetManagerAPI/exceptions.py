from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, (InvalidToken, TokenError)):
        return Response({
            'error': 'Token is invalid or expired',
            'detail': str(exc)
        }, status=status.HTTP_401_UNAUTHORIZED)

    return response
