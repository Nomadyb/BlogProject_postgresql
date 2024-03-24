# except.py

from rest_framework.response import Response
from rest_framework import status
import logging
from rest_framework.exceptions import APIException


def custom_exception_handler(exception, context):

    if isinstance(exception, APIException):
        response_data = {
            "isSuccess": False,
            "message": "An error occurred",
            "error": str(exception.detail),
        }
        status_code = exception.status_code
    else:
        logger = logging.getLogger(__name__)
        logger.error(f"An error occurred: {str(exception)}")

        response_data = {
            "isSuccess": False,
            "message": "An error occurred",
            "error": str(exception),
        }
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return Response(response_data, status=status_code)



