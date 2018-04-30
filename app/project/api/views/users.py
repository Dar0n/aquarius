from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.serializers.user import UserSerializer

from project.api.serializers.users import UserSensitiveInfoSerializer

User = get_user_model()


# @route   GET/POST api/me
# @desc    Get and update user profile
# @access  Public
class GetUpdateUserProfileView(GenericAPIView):
    serializer_class = UserSensitiveInfoSerializer
    permission_classes = [
        IsAuthenticated,
        IsUserOrReadOnly,
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
class AllUsersView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        return Response(UserSerializer(request.user.all(), many=True).data)


# @route   GET api/users/?search=<str:search_string>
# @desc    Search for a user
# @access  Public
class UserProfileView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, user_id):
        return Response(UserSerializer(User.objects.filter(user_id)).data)


# @route   GET api/users/<int:user_id>/
# @desc    Get specific user profile
# @access  Public
class UserProfileView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, user_id):
        return Response(UserSerializer(User.objects.filter(user_id)).data)
