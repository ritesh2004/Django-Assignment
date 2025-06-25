from django.shortcuts import render
from rest_framework.response import Response # Response for API
from rest_framework import viewsets
from rest_framework import generics # generic views for API
from rest_framework import status # status codes for responses

# importing necessary modules
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

# importing models
from .models import TelegramUsers
from django.contrib.auth.models import User

# importing serializers
from .serializers import TelegramUserSerializer, RegisterSerializer, LoginSerializer, UserSerializer

# Create your views here.

# Generate Tokens for User
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# ViewSet for managing Telegram users
class TelegramUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Telegram users.
    """
    query_set = TelegramUsers.objects.all()
    serializer_class = TelegramUserSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        """
        List all Telegram users.
        """
        users = self.query_set
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        """
        Retrieve a specific Telegram user by ID.
        """
        user = self.query_set.filter(id=pk).first()
        if user is None:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """
        Update a specific Telegram user by ID.
        """
        user = self.query_set.filter(id=pk).first()
        if user is None:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
    
# ViewSet for user registration
class RegisterViewSet(generics.CreateAPIView):
    query_set = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    
# ViewSet for user login
class LoginViewSet(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = User.objects.filter(username=username).first()
            if user and user.check_password(password): # Validate user credentials
                tokens = get_tokens_for_user(user)
                user_serialized = UserSerializer(user)
                return Response({"detail": "Login successful", "user": user_serialized.data, "tokens": tokens}, status=status.HTTP_200_OK)
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)