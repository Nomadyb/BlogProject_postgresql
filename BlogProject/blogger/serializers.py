from rest_framework import serializers
from .models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    blog_name = serializers.CharField(max_length=100)
    article = serializers.CharField()
    publish_date = serializers.DateTimeField()
    active = serializers.BooleanField(default=True)
    created_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.blog_name = validated_data.get(
            "blog_name", instance.blog_name)
        instance.article = validated_data.get("article", instance.article)
        instance.publish_date = validated_data.get(
            "publish_date", instance.publish_date)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance
