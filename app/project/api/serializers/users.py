from django.contrib.auth import get_user_model
# from django.core.mail import EmailMessage
from rest_framework import serializers

# from project.restaurant.models import Restaurant, Review, Comment
from project.user.models import Profile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'location', 'things_i_love', 'description', 'joined_date', 'profile_image', 'phone_number']
        read_only_fields = ['id', 'joined_date']


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'user_profile']
        read_only_fields = ['id', 'email']
