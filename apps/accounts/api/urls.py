from django.urls import path
from rest_framework.authtoken import views

from apps.accounts.api.views import UserListAPIView

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('users/', UserListAPIView.as_view()),
]
