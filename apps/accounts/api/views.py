from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView

from apps.accounts.api.serializers import UserSerializer


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
