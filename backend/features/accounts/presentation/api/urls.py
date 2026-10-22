from django.urls import path

from features.accounts.presentation.api.views import (
    create_user,
    get_user_by_id,
)

app_name = "accounts_api"

urlpatterns = [
    path("users/", create_user, name="user-create"),
    path("users/<uuid:user_id>/", get_user_by_id, name="user-detail"),
]