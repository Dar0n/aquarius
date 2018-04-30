from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.user.feed.models import Profile

User = get_user_model()


class UserProfileAdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "followings"]
        read_only_fields = fields


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]
        read_only_fields = fields


class AdvancedUserSerializer(UserSerializer):
    user_profile = UserProfileAdditionSerializer()
    post_count = serializers.SerializerMethodField(
        read_only=True,
    )

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "post_count", "fame_index", "followers", "user_profile"]
        read_only_fields = fields

    def get_post_count(self, user):
        return user.posts.count()


class UserCommentLikesSerializer(UserSerializer):
    comment_likes = serializers.SerializerMethodField(
        read_only=True,
    )

    def get_comment_likes(self, user):
        return sum([p.likes.count() for p in user.posts.all()])


class UserSensitiveInfoSerializer(serializers.ModelSerializer):
    user_profile = UserProfileAdditionSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "followers", "user_profile"]
        read_only_fields = ["id", "username", "followers", "user_profile"]

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
            raise serializers.ValidationError(
                "User with this email address already exists."
            )
        except User.DoesNotExist:
            return value
