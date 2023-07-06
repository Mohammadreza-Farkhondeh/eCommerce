from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', ]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data['email'])
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'is_active', 'is_staff']
