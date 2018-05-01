from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.user.feed.models import Profile

Profile = get_user_model()


class CreateProfileSerializer(serializers.ModelSerializer):
    model = Profile
    fields = ("id", "first_name", "last_name", "email", "username", "user_profile")

    def post(self, validated_data):
        user_profile = Profile.objects.create(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "email", "username", "user_profile"]
        read_only_fields = fields


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name"]
        read_only_fields = fields


class AdvancedUserSerializer(UserSerializer):
    user_profile = Profile.objects.findOne()
    serializer = UserProfileSerializer(many=False)

    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "user_profile"]
        read_only_fields = fields


class UserReviewLikesSerializer(UserSerializer):
    comment_likes = serializers.SerializerMethodField(
        read_only=True,
    )

    def get_review_likes(self, user):
        return sum([p.likes.count() for p in user.posts.all()])


class UserSensitiveInfoSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "email", "username", "user_profile"]
        read_only_fields = ["id", "username", "user_profile"]

    def validate_email(self, value):
        try:
            Profile.objects.get(email=value)
            raise serializers.ValidationError(
                "User with this email address already exists."
            )
        except Profile.DoesNotExist:
            return value
