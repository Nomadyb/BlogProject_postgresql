from datetime import datetime, date 
from blogger.models import Blog
from users.models import User
from django.http import HttpResponseForbidden
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest
from rest_framework.generics import RetrieveAPIView
from .models import Blog


User = get_user_model()


class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        blog_id = request.query_params.get('id')
        blog = get_object_or_404(Blog, pk=blog_id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        if user.role == 'BLOGGER':
            blog_data = {
                'author': user.id,
                'blog_name': request.data.get('blog_name'),
                'article': request.data.get('article'),
                'publish_date': request.data.get('publish_date'),
                'active': request.data.get('active', True)
            }

            serializer = BlogSerializer(data=blog_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponseForbidden("Bu işlemi gerçekleştirmek için yetkiniz yok.")

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




# class BlogDetailView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     def get(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)


# class BlogCreateView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     def post(self, request):
#         user = request.user
#         if user.role == 'BLOGGER':
#             blog_data = {
#                 'author': user.id,
#                 'blog_name': request.data.get('blog_name'),
#                 'article': request.data.get('article'),
#                 'publish_date': request.data.get('publish_date'),
#                 'active': request.data.get('active', True)
#             }

#             serializer = BlogSerializer(data=blog_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return HttpResponseForbidden("Bu işlemi gerçekleştirmek için yetkiniz yok.")





# # TODO:http://localhost:8000/blogger/blog?id=1
# class BlogUpdateView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     def patch(self, request, pk):
#         blog = get_object_or_404(Blog, pk=pk)
#         serializer = BlogSerializer(blog, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BlogDeleteView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     def delete(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         blog.delete()
#         return Response({"response": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
