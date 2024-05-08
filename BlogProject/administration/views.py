
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from blogger.models import Blog , Comment
from .serializers import AdminSerializer
from blogger.serializers import BlogSerializer,CommentSerializer
from users.serializers import *
from datetime import datetime, timezone
from .permissions import IsAdmin
User = get_user_model()



class BloggerViewSet(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [JWTAuthentication]


    def get(self, request):
        user_id = request.query_params.get('id',None)
        if user_id:
            user = get_object_or_404(User, pk=user_id, role='BLOGGER')
            serializer = AdminSerializer(user)
        else:
            blogger_users = User.objects.filter(role="BLOGGER")
            serializer = AdminSerializer(blogger_users, many=True)
        return Response(serializer.data)




    # def get_comments(self, user_id):
    #     user = get_object_or_404(User, pk=user_id, role='BLOGGER')
    #     comments = Comment.objects.filter(author=user)
    #     serializer = CommentSerializer(comments, many=True)
    #     return serializer.data

    # def get(self, request):
    #     user_id = request.query_params.get('id', None)
    #     if user_id:
    #         user = get_object_or_404(User, pk=user_id, role='BLOGGER')
    #         serializer = AdminSerializer(user)
    #         serializer.data['comments'] = self.get_comments(user_id)
    #     else:
    #         blogger_users = User.objects.filter(role="BLOGGER")
    #         serializer = AdminSerializer(blogger_users, many=True)
    #         for data in serializer.data:
    #             # Her bir Blogger kullanıcısının yorumlarını almak için get_comments yöntemini çağırın
    #             data['comments'] = self.get_comments(data['id'])
    #     return Response(serializer.data)






    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def patch(self, request):
        user_id = request.data.get('id')
        user = get_object_or_404(User, pk=user_id, role="BLOGGER")
        serializer = UpdateUserSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user_id = request.query_params.get('id')
        user = get_object_or_404(User, pk=user_id, role="BLOGGER")
        user.delete()
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)





class SetBlogsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        blog_id = request.query_params.get('id')
        if blog_id:
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
        else:#id yoksa hepsini getir
            waiting_blogs = Blog.objects.filter(active=False)
            serializer = BlogSerializer(waiting_blogs, many=True)
            return Response(serializer.data)


""" ilk durum get ve post ile """
# class SetBlogsView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]

#     def get(self, request):
#         waiting_blogs = Blog.objects.filter(active=False)
#         serializer = BlogSerializer(waiting_blogs, many=True)
#         return Response(serializer.data)


#     def post(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         if blog.active:
#             return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)

#         if not blog.publish_date:
#             blog.publish_date = datetime.now()
#             blog.save()

#         blog.active = True
#         blog.save()
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data, status=status.HTTP_200_OK)
