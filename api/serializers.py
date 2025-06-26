from rest_framework import serializers
from .models import TelegramUsers
from django.contrib.auth.models import User
from .task import send_email_task

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Send a welcome email asynchronously using Celery
        send_email_task.delay_on_commit("Welcome to our service", "Thank you for registering!", [user.email])
        return user
 
# Serializer for user login 
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
        
# Serializer for Telegram users
class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUsers
        fields = ['id', 'username', 'createdAt']
        read_only_fields = ['createdAt']
    
    def create(self, validated_data):
        return TelegramUsers.objects.create(**validated_data)