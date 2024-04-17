from rest_framework.permissions import BasePermission , SAFE_METHODS


class IsAdmin(BasePermission):
    """
    Custom permission to only allow bloggers to create, update, and delete blogs.
    """

    def has_permission(self, request, view):
        if  (request.user.is_authenticated and  request.user.role == 'ADMIN'):
            return True
        return False


