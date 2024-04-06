from rest_framework.generics import DestroyAPIView
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model

User = get_user_model()

class BlogDetailView(APIView):
    permission_classes =  [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)



# class BlogCreateView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class BlogCreateView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     def post(self, request):
#         # İstekteki kullanıcıyı otomatik olarak al
#         author = request.user

#         # İsteği alınan kullanıcı ile birlikte serileştirin
#         serializer = BlogSerializer(data=request.data)

#         if serializer.is_valid():
#             # "author" alanını otomatik olarak atayın
#             serializer.save(author=author)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        serializer = BlogSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)
    def patch(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BlogDeleteView(APIView):
#     def delete(self, request):
#         # request.body kullanarak veriyi alıyoruz
#         blog_id = request.data.get('id')
#         if blog_id is None:
#             return Response({'error': 'id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             blog = Blog.objects.get(id=blog_id)
#             blog.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Blog.DoesNotExist:
#             return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)


# class BlogDeleteView(APIView):
#     def delete(self, request):
#         blog_id = request.data.get('id')
#         if blog_id is None:
#             return Response({'error': 'id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             blog = Blog.objects.get(id=blog_id)
#             blog.delete()
#             return Response({'message': 'Blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#         except Blog.DoesNotExist:
#             return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)


class BlogDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# class BlogDeleteView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     def delete(self, request, pk):
#         blog = get_object_or_404(Blog, pk=pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class BlogDeleteView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     def delete(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
