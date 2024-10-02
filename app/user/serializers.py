from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'nombre',
            'primer_apellido',
            'segundo_apellido',
            'imagen',
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8
            }
        }
