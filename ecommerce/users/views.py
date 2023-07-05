from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from .serializers import UserCreateSerializer, UserSerializer


class UserView(APIView):
    """
    An ApiView for user actions, sign-up and retrieve

    Now post and get are supported.
    """

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        """
        user will send email and create account
        """
        email = request.data['email']

        serializer = UserCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.create(serializer.validated_data)
        user = UserSerializer(user)

        return Response(user.data, status.HTTP_201_CREATED)

    @permission_classes([permissions.IsAuthenticated])
    def get(self, request):
        """
        Authenticated user will get email and is_active status
        """
        user = request.user
        try:
            user = UserSerializer(user)
            data = user.data
        except AttributeError as err:
            data = {'user': 'AnonymousUser'}

        return Response(data, status=status.HTTP_200_OK)

    # TODO: apply methods PUT, DELETE
