from django.http.response import JsonResponse
import json
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .serializers import CreateUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
import logging


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            serializer = CreateUserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                refresh = RefreshToken.for_user(user)

                user_data = {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                    "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
                    "is_active": user.is_active,
                }

                logger = logging.getLogger(__name__)
                logger.info(f"New user registered: {user.username}")

                # JSON dosyasından 'key' alındığında hata oluştur
                key = request.data.get('key')
                if key:
                    raise ValueError("Invalid key received")

                return Response(
                    {
                        "isSuccess": True,
                        "message": "Registration successful",
                        "data": user_data,
                        "refresh": str(refresh),
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "isSuccess": False,
                        "message": "Registration failed",
                        "errors": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return custom_exception_handler(e, __name__)
            # #TODO: json dosyadan key geldiğinde hata olan satırı döndür chatgpt ile dene


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            user = authenticate(request, email=email, password=password)

            if user:
                user_data = {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                    "date_joined": user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
                    "is_active": user.is_active,
                }

                refresh = RefreshToken.for_user(user)

                logger = logging.getLogger(__name__)
                logger.info(f"User logged in: {user.username}")

                return Response(
                    {
                        "isSuccess": True,
                        "message": "Login successful",
                        "data": user_data,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token)
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        except Exception as e:
            return custom_exception_handler(e, __name__)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

# TODO: blogger için kullanıcının kendi değerlerini al db'den tüm satırı seç yada kullanıcıya özgü olmalı
# TODO: admin için ise tüm kullanıcılar listelenmeli
# class HomeView(APIView):
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (JWTAuthentication,)

#     def get(self, request):
#         try:
#             return Response(
#                 {
#                     "isSuccess": True,
#                     "message": "Login successful",
#                     "data": request.user.username,

#                 },
#                 status=status.HTTP_200_OK,
#             )


#         except Exception as e:
#             return custom_exception_handler(e, __name__)


# User = get_user_model()
# class HomeView(APIView):
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (JWTAuthentication,)
#     def get(self, request, format=None):
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many=True)
#         return JsonResponse(
#             {
#                 "isSuccess": True,
#                 "message": "Data retrieved successfully",
#                 "data": users_serializer.data,
#             },
#             status=status.HTTP_200_OK,
#         )
"""hello guys"""

User = get_user_model()


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        try:
            if request.user.role == 'BLOGGER':
                user_data = UserSerializer(request.user).data
            elif request.user.role == 'ADMIN':
                queryset = User.objects.all()
                user_data = UserSerializer(queryset, many=True).data
            else:
                return Response(
                    {"error": "Invalid user role"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                {
                    "isSuccess": True,
                    "message": "Data retrieved successfully",
                    "data": user_data,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {"error": "An error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
