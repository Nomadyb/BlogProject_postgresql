# from django.utils.deprecation import MiddlewareMixin
# from django.http import HttpResponseForbidden


# class BloggerMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         if request.user.is_authenticated and request.user.role != 'BLOGGER':
#             return HttpResponseForbidden("You are not authorized to access this resource.")


# from django.http import HttpResponseForbidden
# from users.models import User
# from django.utils.deprecation import MiddlewareMixin


# class RoleCheckMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Kullanıcının oturum açıp açmadığını kontrol edin
#         if request.user.is_authenticated:
#             user = User.objects.get(username=request.user.username)
#             # Kullanıcının rolünü kontrol edin
#             if user.role != 'BLOGGER':
#                 return HttpResponseForbidden("Bu işlemi gerçekleştirmek için yetkiniz yok.")
#         response = self.get_response(request)
#         return response

from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from users.models import User

class RoleCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        User = get_user_model()
        # Kullanıcının oturum açıp açmadığını kontrol edin
        if request.user.is_authenticated:
            # Kullanıcının bir User instance'ı olduğunu kontrol edin
            if isinstance(request.user, User):
                # Kullanıcının rolünü kontrol edin
                if request.user.role != 'BLOGGER':
                    return HttpResponseForbidden("Bu işlemi gerçekleştirmek için yetkiniz yok.")
        response = self.get_response(request)
        return response
