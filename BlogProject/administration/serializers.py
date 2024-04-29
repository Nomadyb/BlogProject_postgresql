from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from collections import defaultdict

# administration/serializers.py



# class AdminSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=150)
#     email = serializers.EmailField(max_length=254)
#     password = serializers.CharField(max_length=128, write_only=True)
#     role = serializers.CharField(max_length=20)
# # is_staff = serializers.BooleanField(default=True)

#     # def create(self, validated_data):
#     #     user = User.objects.create_superuser(**validated_data)
#     #     return user

#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.email = validated_data.get('email', instance.email)
#         instance.set_password(validated_data.get(
#             'password', instance.password))
#         instance.role = validated_data.get('role', instance.role)
#         # instance.is_staff = validated_data.get('is_staff', instance.is_staff)
#         instance.save()
#         return instance


from django.db.models import Count
from blogger.models import Blog
from blogger.models import *
from blogger.serializers import *

from django.contrib.auth import get_user_model

User = get_user_model()
class AdminSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=128, write_only=True)
    role = serializers.CharField(max_length=20)
    waiting_blogs = serializers.SerializerMethodField()
    total_blogs = serializers.SerializerMethodField()
    is_top_blogger = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data.get(
            'password', instance.password))
        instance.role = validated_data.get('role', instance.role)
        # instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()
        return instance

    def get_waiting_blogs(self, obj):
        return Blog.objects.filter(author=obj, active='False').count()

    def get_total_blogs(self, obj):
        return Blog.objects.filter(author=obj).count()

    def get_is_top_blogger(self, obj):
        top_blogger = User.objects.annotate(
            total_blogs=Count('blog')).order_by('-total_blogs').first()
        return obj == top_blogger



    # def get_comments(self,obj):
    #     return Comment.objects.filter(author=obj).count()

    def get_comments(self, obj):
        # Kullanıcının yorumlarını al
        comments = Comment.objects.filter(author=obj)

        # Yorumların bulunduğu blogların bilgilerini toplamak için bir sözlük oluştur
        blog_comments = defaultdict(list)
        for comment in comments:
            blog_comments[comment.has].append(comment)

        # Blog ve yorum bilgilerini uygun şekilde serileştir
        serialized_data = []
        for blog, comments in blog_comments.items():
            blog_serializer = BlogSerializer(blog)
            comment_serializer = CommentSerializer(comments, many=True)
            serialized_data.append({
                'blog': blog_serializer.data,
                'comments': comment_serializer.data
            })

        return serialized_data
