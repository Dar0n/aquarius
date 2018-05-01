from django.contrib.auth import get_user_model
# from django.core.mail import EmailMessage
from rest_framework import serializers

from project.restaurant.models import Restaurant, Review, Comment
from project.user.models import Profile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'location', 'things_i_love', 'description', 'joined_date', 'profile_image']
        read_only_fields = ['id', 'joined_date']


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'user_profile']
        read_only_fields = ['id', 'email']

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
