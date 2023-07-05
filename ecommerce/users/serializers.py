from rest_framework.serializers import ModelSerializer, as_serializer_error
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', ]

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'])
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'is_active', 'is_staff']
