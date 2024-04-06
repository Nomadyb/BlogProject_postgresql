from rest_framework import serializers
from .models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()


# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     blog_name = serializers.CharField(max_length=100)
#     article = serializers.CharField()
#     #TODO: publish date olmasın update_date , active not true 
#     # publish_date = serializers.DateTimeField(allow_null=True, required=False)
#     update_date = serializers.DateTimeField(read_only=True)
#     active = serializers.BooleanField(default=False)
#     created_date = serializers.DateTimeField(read_only=True)
#     # update_date = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.blog_name = validated_data.get(
#             "blog_name", instance.blog_name)
#         instance.article = validated_data.get("article", instance.article)
#         instance.publish_date = validated_data.get(
#             "publish_date", instance.publish_date)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    blog_name = serializers.CharField(max_length=100)
    article = serializers.CharField()
    update_date = serializers.DateTimeField(read_only=True)
    active = serializers.BooleanField(default=False)
    created_date = serializers.DateTimeField(read_only=True)
    publish_date = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.blog_name = validated_data.get(
            "blog_name", instance.blog_name)
        instance.article = validated_data.get("article", instance.article)
        instance.active = validated_data.get("active", instance.active)
        instance.publish_date = validated_data.get("publish_date", instance.publish_date)

        instance.save()
        return instance

    # def get_username(self, obj):
    #     return obj.author.username
