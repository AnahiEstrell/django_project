from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema

from user.serializers import UserSerializer
from user.models import User

@extend_schema(tags=['User'])
class UserViewSet(viewsets.ModelViewSet):
    """CRUD for user in the systems"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]
