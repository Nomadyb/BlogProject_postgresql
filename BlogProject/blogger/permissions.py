from rest_framework.permissions import BasePermission


class IsBlogger(BasePermission):
    """
    Custom permission to only allow bloggers to create a blog.
    """

    def has_permission(self, request, view):
        return request.user.role == 'BLOGGER'
