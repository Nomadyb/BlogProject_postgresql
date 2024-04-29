from datetime import datetime, date ,time
from django.http import HttpResponseForbidden
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from .serializers import BlogSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .permissions import IsBlogger
from blogger.models import User
from blogger.models import Blog, Comment

User = get_user_model()


class BlogView(APIView):
    # permission_classes = [IsAuthenticated, IsBlogger]
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        try:
            blog_id = request.query_params.get('id')
            blog = get_object_or_404(Blog, pk=blog_id)
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        try:
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
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        try:
            blog_id = request.query_params.get('id')
            blog = get_object_or_404(Blog, pk=blog_id)
            serializer = BlogSerializer(blog, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            blog_id = request.query_params.get('id')
            blog = get_object_or_404(Blog, pk=blog_id)
            blog.delete()
            return Response({"response": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



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


"""
Comment işlemleri
"""

# class CommentView(APIView):
#    pass 




class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)


    def get(self, request):
        comment_id = request.query_params.get('comment_id')
        if comment_id is None:
            return Response({"error": "Missing 'comment_id' query parameter."}, status=status.HTTP_400_BAD_REQUEST)

        comment = get_object_or_404(Comment, pk=comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=200)

    def post(self, request):
            try:
                blog_id = request.query_params.get('blog_id')
                if blog_id is None:
                    return Response({"error": "Missing 'blog_id' query parameter."}, status=status.HTTP_400_BAD_REQUEST)

                blog = get_object_or_404(Blog, id=blog_id)

                serializer = CommentSerializer(
                    data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save(author=request.user, has=blog)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def patch(self, request):
        try:
            comment_id = request.query_params.get('comment_id')
            if comment_id is None:
                return Response({"error": "Missing 'comment_id' query parameter."}, status=status.HTTP_400_BAD_REQUEST)

            comment = get_object_or_404(Comment, pk=comment_id)
            serializer = CommentSerializer(
                comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            comment_id = request.query_params.get('comment_id')
            if comment_id is None:
                return Response({"error": "Missing 'comment_id' query parameter."}, status=status.HTTP_400_BAD_REQUEST)

            comment = get_object_or_404(Comment, pk=comment_id)
            comment.delete()
            return Response({"response": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



