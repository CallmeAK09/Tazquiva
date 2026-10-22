from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from features.accounts.presentation.api.views import (
    change_password,
    create_user,
    get_user_by_id,
    login,
)

app_name = "accounts_api"

urlpatterns = [
    path("users/", create_user, name="user-create"),
    path("users/<uuid:user_id>/", get_user_by_id, name="user-detail"),
    path("users/change-password/", change_password, name="user-change-password"),
    path("login/", login, name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]