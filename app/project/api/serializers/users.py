from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework import serializers

from project.restaurant.feed.models import Restaurant, Review, Comment
from project.user.feed.models import Profile

User = get_user_model()


class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "first_name", "last_name", "email", "username", "user_profile")

    def post(self, validated_data):
        user_profile = Profile.objects.create(**validated_data)
        return user_profile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'things_i_love', 'description', 'joined_date', 'profile_image']
        # read_only_fields = fields


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'things_i_love', 'description', 'joined_date', 'profile_image']
        # read_only_fields = fields

    # @staticmethod
    # def send_notification(**kwargs):
    #     requester = kwargs.get('reviewer')
    #     receiver = kwargs.get('reviewed')
    #     message = EmailMessage(
    #         subject='You have been reviewed',
    #         body=f'The user {requester.username} has reviewed your restaurant',
    #         to=[receiver.email],
    #     )
    #     message.send()
    #
    # def save(self, **kwargs):
    #     f_request = Review.objects.create(**kwargs)
    #     self.send_notification(**kwargs)
    #     return f_request


class CreateCommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ("id", "user", "review", "content")

    @staticmethod
    def post(validated_data):
        user_comment = Comment.objects.create(**validated_data)
        return user_comment


class CreateCommentsOnReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ("id", "user", "review", "content", "date_created", "date_modified", "likes")

    @staticmethod
    def post(validated_data):
        user_comment = Comment.objects.create(**validated_data)
        return user_comment
