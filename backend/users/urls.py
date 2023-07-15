from django.urls import path
from .views import UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView, )

app_name = 'users'

urlpatterns = [
    path('', UserView.as_view()), # Post email to create account and GET to retrieve user information
    path('token', TokenObtainPairView.as_view()),  # POST email and password to obtain pair token
    path('token/refresh/', TokenRefreshView.as_view()),  # POST refresh token to obtain a new access token
    path('token/verify/', TokenVerifyView.as_view()),  # POST access token to verify
]
