from rest_framework import (
    viewsets,
    permissions,
    generics,
)
from drf_spectacular.utils import extend_schema

from user.serializers import UserSerializer
from user.models import User


@extend_schema(tags=['User'])
class UserViewSet(viewsets.ModelViewSet):
    """CRUD for user in the systems"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]


@extend_schema(tags=['Me'])
class UserMeView(generics.RetrieveUpdateAPIView):
    """ View for authenticated user. """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """ Retrieve and return the authenticated user. """
        return self.request.user
