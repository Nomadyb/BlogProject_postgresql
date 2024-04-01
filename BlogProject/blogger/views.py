from datetime import datetime, date ,time
from blogger.models import Blog
from users.models import User
from django.http import HttpResponseForbidden
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .permissions import IsBlogger

User = get_user_model()


class BlogView(APIView):
    # permission_classes = [IsAuthenticated, IsBlogger]
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        blog_id = request.query_params.get('id')
        blog = get_object_or_404(Blog, pk=blog_id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

#first
    # def post(self, request):
    #     user = request.user
    #     if user.role == 'BLOGGER':
    #         blog_data = {
    #             'author': user,
    #             'blog_name': request.data.get('blog_name'),
    #             'article': request.data.get('article'),
    #             'update_date': datetime.now(),  # Set update_date to current date and time
    #             'active': request.data.get('active', True)
    #         }

    #         serializer = BlogSerializer(
    #             data=blog_data, context={'request': request})
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return HttpResponseForbidden("Bu işlemi gerçekleştirmek için yetkiniz yok.")

#two
    # def post(self, request):
    #     serializer = BlogSerializer(
    #         data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save(author=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        request_data = request.data
        if request.user.role == 'BLOGGER':
            serializer = BlogSerializer(
                data=request_data, context={'request': request})
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)


    def patch(self, request):
        blog_id = request.query_params.get('id')
        blog = get_object_or_404(Blog, pk=blog_id)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        blog_id = request.query_params.get('id')
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.delete()
        return Response({"response": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# class BlogCreateView(APIView):
#     authentication_classes = (JWTAuthentication,)
#     permission_classes = [IsAuthenticated, IsBlogger]

#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BlogDetailView(APIView):
#     authentication_classes = (JWTAuthentication,)
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)

#     def patch(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         serializer = BlogSerializer(blog, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         blog.delete()
#         return Response({"response": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
