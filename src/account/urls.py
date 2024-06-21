from django.urls import path
from .views import RegisterView, ManageView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Endpoint for obtaining a pair of access and refresh tokens during user login
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    # Endpoint for refreshing the access token using the refresh token
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Endpoint for user registration
    path("api/register/", RegisterView.as_view(), name="sign_up"),

    # Endpoint for managing user data (retrieve, update, destroy)
    path("api/manage/", ManageView.as_view(), name="manage_user"),
]
