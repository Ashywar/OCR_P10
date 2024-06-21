from rest_framework import serializers
from .models import UserData


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
            "birthdate",
            "can_be_contacted",
            "can_data_be_shared",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        """
        Create and return a new user instance, given the validated data.
        """
        user = UserData.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            birthdate=validated_data["birthdate"],
            can_be_contacted=validated_data["can_be_contacted"],
            can_data_be_shared=validated_data["can_data_be_shared"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["id", "first_name", "last_name", "email"]


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = [
            "id",
            "first_name",
            "last_name",
            "birthdate",
            "can_be_contacted",
            "can_data_be_shared",
        ]
