from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    role=serializers.CharField()

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user 
    