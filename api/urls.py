from django.urls import path
from .views import TelegramUserViewSet, RegisterViewSet, LoginViewSet

# Define URL patterns for the API
# This file contains the URL routing for the API endpoints related to Telegram users, registration, and login.
# Each path is associated with a specific viewset that handles the request and response logic.
urlpatterns = [
    path('users/', TelegramUserViewSet.as_view({'get': 'list', 'post': 'create'}), name='telegram-user-list'),
    path('users/<int:pk>/', TelegramUserViewSet.as_view({'get': 'retrieve', 'put' : 'update'}), name='telegram-user-detail'),
    path('register/', RegisterViewSet.as_view(), name='register'),
    path('login/', LoginViewSet.as_view(), name='login'),
]