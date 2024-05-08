from .encryption_utils import encrypt_image, decrypt_image
from django.conf import settings
import base64
from rest_framework import serializers
from .models import Blog, Comment
from django.contrib.auth import get_user_model
from django.db import DatabaseError

User = get_user_model()

#    def get_comments(self, obj):
#        return Comment.objects.filter(author=obj).count()

# class BlogSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     blog_name = serializers.CharField(max_length=100)
#     article = serializers.CharField()
#     update_date = serializers.DateTimeField(read_only=True)
#     active = serializers.BooleanField(default=False)
#     created_date = serializers.DateTimeField(read_only=True)
#     publish_date = serializers.DateTimeField(required=False)
#     image = serializers.ImageField(required=False)  # Görüntü alanını ekle

#     def create(self, validated_data):
#         try:
#             return Blog.objects.create(**validated_data)
#         except DatabaseError:
#             raise serializers.ValidationError("Database error occurred")

#     def update(self, instance, validated_data):
#         try:
#             instance.blog_name = validated_data.get(
#                 "blog_name", instance.blog_name)
#             instance.article = validated_data.get("article", instance.article)
#             instance.active = validated_data.get("active", instance.active)
#             instance.publish_date = validated_data.get(
#                 "publish_date", instance.publish_date)
#             instance.image = validated_data.get(
#                 "image", instance.image)  # Görüntü alanını güncelle
#             instance.save()
#             return instance
#         except DatabaseError:
#             raise serializers.ValidationError("Database error occurred")

"""
use-1
"""
# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     blog_name = serializers.CharField(max_length=100)
#     article = serializers.CharField()
#     update_date = serializers.DateTimeField(read_only=True)
#     active = serializers.BooleanField(default=False)
#     created_date = serializers.DateTimeField(read_only=True)
#     publish_date = serializers.DateTimeField(required=False)
#     image = serializers.ImageField(required=False)  

#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance

"""
AES
"""

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    blog_name = serializers.CharField(max_length=100)
    article = serializers.CharField()
    update_date = serializers.DateTimeField(read_only=True)
    active = serializers.BooleanField(default=False)
    created_date = serializers.DateTimeField(read_only=True)
    publish_date = serializers.DateTimeField(required=False)
    #TODO: değiştir image yapısını 
    image = serializers.ImageField(required=False)

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        if image:
            encrypted_image = encrypt_image(image.path, settings.KEY)
            validated_data['image'] = encrypted_image
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        image = validated_data.pop('image', None)
        if image:
            encrypted_image = encrypt_image(image.path, settings.KEY)
            validated_data['image'] = encrypted_image
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

"""
useless
"""
# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     blog_name = serializers.CharField(max_length=100)
#     article = serializers.CharField()
#     update_date = serializers.DateTimeField(read_only=True)
#     active = serializers.BooleanField(default=False)
#     created_date = serializers.DateTimeField(read_only=True)
#     publish_date = serializers.DateTimeField(required=False)
#     image = serializers.ImageField(required=False)

#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         if instance.image:
#             ret['image'] = self.encode_image(instance.image)
#         return ret

#     def encode_image(self, image):
#         with open(image.path, 'rb') as f:
#             encoded_string = base64.b64encode(f.read()).decode('utf-8')
#         return encoded_string



#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance




# class CommentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     has = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())
#     author = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     comments = serializers.CharField()
#     created_date = serializers.DateTimeField(read_only=True)
#     updated_date = serializers.DateTimeField(read_only=True)

#     def create(self,validated_data):
#         return Comment.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance




class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    has = serializers.PrimaryKeyRelatedField(
        queryset=Blog.objects.all(), required=False)
    #TODO: id'yi al query olarak 
    comments = serializers.CharField()
    author = serializers.CharField(
        source='author.username', read_only=True)  # Yazarın adını almak için
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        author = self.context['request'].user
        validated_data['author'] = author

        return Comment.objects.create(**validated_data)


    # def create(self, validated_data):
    #     # Yazarı doğrudan validated_data'dan al
    #     author = validated_data.pop('author', None)
    #     # Yazar bilgisi yoksa veya geçersizse hata fırlat
    #     if not author:
    #         raise serializers.ValidationError("Author information is missing.")
    #     # Gelen kullanıcı adına sahip kullanıcıyı bul
    #     user = User.objects.filter(username=author).first()
    #     if not user:
    #         raise serializers.ValidationError("Invalid author username.")
    #     validated_data['author'] = user
    #     return Comment.objects.create(**validated_data)


    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
