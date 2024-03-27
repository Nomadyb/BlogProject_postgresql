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


User = get_user_model()





# class BlogDetailView(RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = 'pk'  # Use 'pk' as the lookup field

#     def get(self, request, *args, **kwargs):
#         blog = self.get_object()  # Retrieve the blog object
#         serializer = self.get_serializer(blog)  # Serialize the blog object
#         return Response(serializer.data)  # Return the serialized data


class BlogDetailView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)




class BlogCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        user = request.user
        if user.role == 'BLOGGER':
            # Get publish_date from request data
            publish_date = request.data.get('publish_date')
            try:
                # Convert publish_date to date object
                publish_date = datetime.strptime(
                    publish_date, "%Y-%m-%d").date()
            except ValueError:
                return Response({'error': 'Invalid date format for publish_date'}, status=status.HTTP_400_BAD_REQUEST)

            blog_data = {
                'author': user,
                'blog_name': request.data.get('blog_name'),
                'article': request.data.get('article'),
                'publish_date': publish_date,
                'active': request.data.get('active', True)
            }

            serializer = BlogSerializer(
                data=blog_data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponseForbidden("Bu işlemi gerçekleştirmek için yetkiniz yok.")






# TODO:http://localhost:8000/blogger/blog?id=1
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


class BlogDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response({"response": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
