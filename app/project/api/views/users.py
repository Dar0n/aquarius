from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.serializers.users import UserSerializer, AdvancedUserSerializer

User = get_user_model()


# @route   GET/POST api/me
# @desc    Get and update user profile
# @access  Public
class GetUpdateUserProfileView(GenericAPIView):
    serializer_class = AdvancedUserSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, request, **kwargs):
        return Response(self.get_serializer(request.user).data)

    def post(self, request, **kwargs):
        serializer = self.get_serializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(self.get_serializer(user).data)


# @route   GET api/users/list/
# @desc    Get all users
# @access  Public
class GetAllUsersView(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, request):
        return Response(UserSerializer(request.user.all(), many=True).data)


# @route   GET api/users/?search=<str:search_string>
# @desc    Search for a user
# @access  Public
class GetUserView(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, user_id):
        return Response(UserSerializer(User.objects.filter(user_id)).data)


# @route   GET api/users/<int:user_id>/
# @desc    Get specific user profile
# @access  Public
class GetSpecificUserProfileView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, user_id):
        return Response(UserSerializer(User.objects.filter(user_id)).data)
