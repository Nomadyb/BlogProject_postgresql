# administration/views.py
# administration/views.py
# from django.shortcuts import get_object_or_404
# from rest_framework import viewsets
# from rest_framework.response import Response
# from blogger.models import Blog  # blogger uygulamasından Blog modelini içe aktar
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.generics import DestroyAPIView
# from rest_framework.views import APIView
# from django.views.decorators.csrf import csrf_protect
# # class AdminBlogViewSet(viewsets.ViewSet):
# from django.views.decorators.csrf import csrf_exempt
# from blogger.serializers import BlogSerializer



# class AdminBlogViewSet(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     # def list(self, request):
#     #     blogs = Blog.objects.all()
#     #     return Response({'blogs': blogs})

#     def list(self,request):
#         blogs = Blog.objects.filter(active__isnull=True)
#         serializer = BlogSerializer(blogs,many=True)
#         return Response(serializer.data)



#     def retrieve(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         return Response({'blog': blog})

#     def update(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         # Request'ten gelen veriyi kullanarak blog durumunu güncelle
#         blog.status = request.data.get('status', blog.status)
#         blog.save()
#         return Response({'status': 'Blog status updated'})

#     def destroy(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         blog.delete()
#         return Response({'status': 'Blog deleted'})


# class AdminBlogViewSet(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     def get(self, request):
#         blogs = Blog.objects.filter(active__isnull=True)
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         # Burada bir blog oluşturma işlemi gerçekleştirebilirsiniz
#         pass

#     def put(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         blog.status = request.data.get('status', blog.status)
#         blog.save()
#         return Response({'status': 'Blog status updated'})

#     def delete(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         blog.delete()
#         return Response({'status': 'Blog deleted'})








# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework import viewsets
# from django.shortcuts import get_object_or_404
# from blogger.models import Blog
# from .serializers import AdminSerializer


# class BloggerViewSet(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (JWTAuthentication,)

#     queryset = Blog.objects.all()
#     serializer_class = AdminSerializer

#     def list(self, request):
#         queryset = self.queryset
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request):
#         pk = request.query_params.get('id')
#         blog = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(blog)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request):
#         pk = request.query_params.get('id')
#         blog = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request):
#         pk = request.query_params.get('id')
#         blog = get_object_or_404(self.queryset, pk=pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from blogger.models import Blog
# from .serializers import BlogSerializer
# from .views import BlogSerializer


# class BloggerViewSet(APIView):
#     permission_classes = [IsAuthenticated]  # Gerekli izinleri ayarlayın
#     # Gerekli kimlik doğrulama yöntemlerini ayarlayın
#     authentication_classes = [JWTAuthentication]

#     def get(self, request):
#         # Tüm blogger'ları listele
#         bloggers = Blog.objects.all()
#         serializer = BlogSerializer(bloggers, many=True)
#         return Response(serializer.data)

#     def get_blog(self, request):
#         # Belirli bir blogun ayrıntılarını getir
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)

#     def post(self, request):
#         # Yeni bir blog oluştur
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request):
#         # Var olan bir blogu güncelle
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         serializer = BlogSerializer(blog, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request):
#         # Var olan bir blogu sil
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def get_waiting_blogs(self, request):
#         # Yayın için bekleyen tüm blogları listele
#         waiting_blogs = Blog.objects.filter(status='waiting')
#         serializer = BlogSerializer(waiting_blogs, many=True)
#         return Response(serializer.data)

#     def approve_blog(self, request):
#         # Blogu yayına al
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         blog.status = 'approved'
#         blog.save()
#         return Response({"message": "Blog approved successfully"}, status=status.HTTP_200_OK)
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from blogger.models import Blog
from .serializers import *
from blogger.serializers import BlogSerializer
from users.serializers import * 

User = get_user_model()


# class BloggerViewSet(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]

# #   blogger_blogs = []
# # for loop kullan userların içinde döndür
# #      blogs= = blog.object.filter()


#     # def get(self, request):
#     #     blogs = Blog.objects.all()
#     #     serializer = BlogSerializer(blogs, many=True)
#     #     return Response(serializer.data)

#     def get(self, request):
#         blogger_users = User.objects.filter(role="BLOGGER")
#         serializer = AdminSerializer(blogger_users, many=True)
#         return Response(serializer.data)




#     def get_blog(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         serializer = AdminSerializer(blog)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = AdminSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         serializer = AdminSerializer(blog, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def get_waiting_blogs(self, request):
#         waiting_blogs = Blog.objects.filter(status='waiting')
#         serializer = AdminSerializer(waiting_blogs, many=True)
#         return Response(serializer.data)


#     # def approve_blog(self, request):
#     #     blog_id = request.query_params.get('id')
#     #     blog = get_object_or_404(Blog, pk=blog_id)
#     #     blog.active = True
#     #     blog.save()
#     #     return Response({"message": "Blog activated successfully"}, status=status.HTTP_200_OK)
#     # def approve_blog(self, request):
#     #     blog_id = request.query_params.get('id')
#     #     blog = get_object_or_404(Blog, pk=blog_id)
#     #     if blog.active:
#     #         return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)
#     #     blog.active = True
#     #     blog.save()
#     #     return Response({"message": "Blog activated successfully"}, status=status.HTTP_200_OK)

#     # def approve_blog(self, request, *args, **kwargs):
#     #     if 'id' in request.query_params:
#     #         return self.approve_blog(request)
#     #     else:
#     #         blogger_users = User.objects.filter(role="BLOGGER")
#     #         serializer = AdminSerializer(blogger_users, many=True)
#     #         return Response(serializer.data)
    
#     # def approve_blog(self, request, *args, **kwargs):
#     #     blog_id = request.query_params.get('id')
#     #     blog = get_object_or_404(Blog, pk=blog_id)
#     #     if blog.active:
#     #         return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)
#     #     blog.active = True
#     #     blog.save()
#     #     return Response({"message": "Blog activated successfully"}, status=status.HTTP_200_OK)


#     # def approve_blog(self, request, *args, **kwargs):
#     #     blog_id = request.query_params.get('id')
#     #     blog = get_object_or_404(Blog, pk=blog_id)
#     #     if blog.active:
#     #         return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)
#     #     blog.active = True
#     #     blog.save()
#     #     # BlogSerializer ile blog nesnesini serialize edin
#     #     serializer = BlogSerializer(blog)
#     #     return Response({"message": "Blog activated successfully", "blog": serializer.data}, status=status.HTTP_200_OK)


#     # def approve_blog(self, request, *args, **kwargs):
#     #     blog_id = request.query_params.get('id')
#     #     blog = get_object_or_404(Blog, pk=blog_id)
#     #     if blog.active:
#     #         return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)
#     #     blog.active = True
#     #     blog.save()
#     #     # BlogSerializer ile blog nesnesini serialize edin
#     #     serializer = BlogSerializer(blog)
#     #     return Response({"message": "Blog activated successfully", "blog": serializer.data}, status=status.HTTP_200_OK)

#     # def approve_blog(self, request, *args, **kwargs):
#     #     blog_id = request.query_params.get('id')
#     #     blog = get_object_or_404(Blog, pk=blog_id)
#     #     if blog.active:
#     #         return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)
#     #     blog.active = True
#     #     blog.save()
#     #     # BlogSerializer ile blog nesnesini serialize edin
#     #     serializer = BlogSerializer(blog)
#     #     return Response({"message": "Blog activated successfully", "blog": serializer.data}, status=status.HTTP_200_OK)

#     def approve_blog(self, request, *args, **kwargs):
#         blog_id = request.query_params.get('id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         if blog.active:
#             return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)
#         blog.active = True
#         blog.save()
#         return Response({"message": "Blog activated successfully", "id": blog.id}, status=status.HTTP_200_OK)


class BloggerViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        blogger_users = User.objects.filter(role="BLOGGER")
        serializer = BlogSerializer(blogger_users, many=True)
        return Response(serializer.data)

    def get_blog(self, request):
        blog_id = request.query_params.get('id')
        blog = get_object_or_404(Blog, pk=blog_id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_waiting_blogs(self, request):
        waiting_blogs = Blog.objects.filter(status='waiting')
        serializer = BlogSerializer(waiting_blogs, many=True)
        return Response(serializer.data)

    def approve_blog(self, request, *args, **kwargs):
        blog_id = request.query_params.get('id')
        blog = get_object_or_404(Blog, pk=blog_id)
        if blog.active:
            return Response({"message": "Blog is already active"}, status=status.HTTP_200_OK)
        blog.active = True
        blog.save()
        return Response({"message": "Blog activated successfully", "id": blog.id}, status=status.HTTP_200_OK)
