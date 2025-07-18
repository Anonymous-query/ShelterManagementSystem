from django.contrib import admin
from django.urls import path
from .apis import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='user_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', RegisterView.as_view(), name='register'),
]