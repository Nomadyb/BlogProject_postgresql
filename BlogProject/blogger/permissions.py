from rest_framework.permissions import BasePermission , SAFE_METHODS


class IsBlogger(BasePermission):
    """
    Custom permission to only allow bloggers to create, update, and delete blogs.
    """

    def has_permission(self, request, view):
        if  (request.user.is_authenticated and  request.user.role == 'BLOGGER'):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Sadece objenin sahibi (yazarı) blogu güncelleme ve silme işlemi yapabilir
        return obj.author == request.user
