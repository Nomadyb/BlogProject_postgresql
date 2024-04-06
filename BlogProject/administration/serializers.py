from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


# administration/serializers.py



class AdminSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=128, write_only=True)
    role = serializers.CharField(max_length=20)
# is_staff = serializers.BooleanField(default=True)

    # def create(self, validated_data):
    #     user = User.objects.create_superuser(**validated_data)
    #     return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data.get(
            'password', instance.password))
        instance.role = validated_data.get('role', instance.role)
        # instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()
        return instance


