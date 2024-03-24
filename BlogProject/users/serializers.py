from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model






"""
    son durum
"""


# serializers.py


User = get_user_model()


class IdSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=70)
    role = serializers.ChoiceField(
        choices=["ADMIN", "BLOGGER"], default="BLOGGER"
    )
    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        email = attrs.get("email")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "Bu e-posta adresi zaten kullanılıyor."
            )

        try:
            validate_email(email)
        except ValidationError:
            raise serializers.ValidationError("Geçersiz e-posta adresi.")

        password = attrs.get("password")

        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)

        return attrs



class UpdateUserSerializer(IdSerializer):
    username = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(max_length=70, required=False)
    role = serializers.ChoiceField(
        choices=["ADMIN", "BLOGGER"], default="BLOGGER", required=False)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.role = validated_data.get("role", instance.role)
        instance.save()
        return instance


User = get_user_model()


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    last_login = serializers.DateTimeField()
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=254)
    role = serializers.CharField(max_length=100)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        return {
            "id": data["id"],
            "last_login": data["last_login"],
            "username": data["username"],
            "first_name": data["first_name"],
            "email": data["email"],
            "role": data["role"],

        }


