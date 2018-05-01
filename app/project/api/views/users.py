from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.serializers.users import UserSerializer, UserProfileSerializer

User = get_user_model()


# @route   GET/POST api/me
# @desc    Get and update user profile
# @access  Public
class GetUpdateUserProfileView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    # def get(self, request):
    #     return

    # def get(self, request):
    #     user = User.objects.filter(user_id=request.id)
    #     return Response(self.get_serializer(user).data)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def post(self, request):
        me = User.objects.get(id=request.user.id)
        serializer = UserSerializer(me, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # def post(self, request, **kwargs):
    #     serializer = self.get_serializer(request.user, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     return Response(self.get_serializer(user).data)


# @route   GET api/users/list/
# @desc    Get all users
# @access  Public
class GetAllUsersView(APIView):
    serializer_class = UserSerializer
    # queryset = User.objects.all()
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, request):
        return Response(UserSerializer(User.objects.all()).data)


# @route   GET api/users/?search=<str:search_string>
# @desc    Search for a user
# @access  Public
class GetUserView(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, user_id):
        users = User.objects.all()
        return Response(users)


# @route   GET api/users/<int:user_id>/
# @desc    Get specific user profile
# @access  Public
class GetSpecificUserProfileView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, user_id):
        return Response(UserSerializer(User.objects.filter(user_id)).data)
