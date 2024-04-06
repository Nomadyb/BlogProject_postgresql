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


# from django.http import HttpResponseForbidden
# from django.contrib.auth import get_user_model
# from users.models import User

# class RoleCheckMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         User = get_user_model()
#         if request.user.is_authenticated:
#             if isinstance(request.user, User):
#                 if request.user.role != 'BLOGGER':
#                     return HttpResponseForbidden("Bu işlemi gerçekleştirmek için yetkiniz yok.")
#         response = self.get_response(request)
#         return response


# from django.http import HttpResponseForbidden
# from django.contrib.auth import get_user_model
# from users.models import User


# class RoleCheckMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         User = get_user_model()

#         # CSRF korumasını devre dışı bırak
#         setattr(request, '_dont_enforce_csrf_checks', True)

#         if request.user.is_authenticated:
#             if isinstance(request.user, User):
#                 if request.user.role != 'BLOGGER':
#                     return HttpResponseForbidden("Bu işlemi gerçekleştirmek için yetkiniz yok.")
#         response = self.get_response(request)
#         return response


from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from users.models import User
import traceback


class RoleCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        User = get_user_model()

        # CSRF korumasını devre dışı bırak
        setattr(request, '_dont_enforce_csrf_checks', True)

        if request.user.is_authenticated:
            if isinstance(request.user, User):
                if request.user.role != 'BLOGGER':
                    return HttpResponseForbidden("Bu işlemi gerçekleştirmek için yetkiniz yok.")

        try:
            response = self.get_response(request)
        except Exception as e:
            print("Middleware'da bir hata oluştu:")
            print(traceback.format_exc())
            response = HttpResponseForbidden(
                "Middleware'da bir hata oluştu. Lütfen sistem yöneticinizle iletişime geçin.")

        return response
