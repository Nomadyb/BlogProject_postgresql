
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from blogger.models import Blog
from .serializers import AdminSerializer
from blogger.serializers import BlogSerializer
from users.serializers import * 
from datetime import datetime , timezone

User = get_user_model()


# class BloggerDetailView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]

#     def get(self, request):
#         user_id = request.query_params.get('id')
#         user = get_object_or_404(User, pk=user_id, role='BLOGGER')
#         serializer = UserSerializer(user)
#         return Response(serializer.data)




class BloggerViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        blogger_users = User.objects.filter(role="BLOGGER")
        serializer = AdminSerializer(blogger_users, many=True)
        return Response(serializer.data)


    def get_blog(self, request):
        user_id = request.query_params.get('id')
        user = get_object_or_404(User, pk=user_id, role='BLOGGER')
        serializer = UserSerializer(user) 
        return Response(serializer.data)



    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request):
    #     user_id = request.query_params.get('id')
    #     user = get_object_or_404(User, pk=user_id)
    #     serializer = UpdateUserSerializer(
    #         user, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request):
        user_id = request.data.get('id')
        user = get_object_or_404(User, pk=user_id, role="BLOGGER")
        serializer = UpdateUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




 







    def delete(self, request):
        user_id = request.query_params.get('id')
        user = get_object_or_404(User, pk=user_id, role="BLOGGER")
        user.delete()
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



    # def get_waiting_blogs(self, request):
    #     waiting_blogs = Blog.objects.filter(status='waiting')
    #     serializer = BlogSerializer(waiting_blogs, many=True)
    #     return Response(serializer.data)


    # def get_waiting_blogs(self, request):
    #     waiting_blogs = Blog.objects.filter(active=False)
    #     serializer = BlogSerializer(waiting_blogs, many=True)
    #     return Response(serializer.data)



    # def approve_blog(self, request, *args, **kwargs):
    #     blog_id = request.query_params.get('id')
    #     blog = get_object_or_404(Blog, pk=blog_id)
    #     if blog.active:
    #         return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)
    #     blog.active = True
    #     blog.save()
    #     return Response({"message": "Blog activated successfully", "id": blog.id}, status=status.HTTP_200_OK)


class SetBlogsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        waiting_blogs = Blog.objects.filter(active=False)
        serializer = BlogSerializer(waiting_blogs, many=True)
        return Response(serializer.data)
    
    # def post(self, request, *args, **kwargs):
    #     blog_id = request.query_params.get('id')
    #     blog = get_object_or_404(Blog, pk=blog_id)
    #     if blog.active:
    #         return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)
    #     blog.active = True
    #     blog.save()
    #     return Response({"message": "Blog activated successfully", "id": blog.id}, status=status.HTTP_200_OK)

    # def post(self, request):
    #     blog_id = request.data.get('id')
    #     blog = get_object_or_404(Blog, pk=blog_id)
    #     if blog.active:
    #         return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)

    #     # Set publish_date if it's not already set
    #     if not blog.publish_date:
    #         # You might need to import timezone from django.utils
    #         blog.publish_date = timezone.now()
    #         blog.save()

    #     blog.active = True
    #     blog.save()
    #     serializer = BlogSerializer(blog)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


    # def post(self, request):
    #     blog_id = request.query_params.get('id')
    #     blog = get_object_or_404(Blog, pk=blog_id)
    #     if blog.active:
    #         return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)

    #     # Set publish_date if it's not already set
    #     if not blog.publish_date:
    #         blog.publish_date = timezone.now()
    #         blog.save()

    #     blog.active = True
    #     blog.save()
    #     serializer = BlogSerializer(blog)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        blog_id = request.query_params.get('id')
        blog = get_object_or_404(Blog, pk=blog_id)
        if blog.active:
            return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)

        if not blog.publish_date:
            blog.publish_date = datetime.now()
            blog.save()

        blog.active = True
        blog.save()
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
