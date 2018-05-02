from django.contrib.auth import get_user_model
# from django.core.mail import EmailMessage
# from django.forms import ImageField
from rest_framework import serializers

# from project.restaurant.models import Restaurant, Review, Comment
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


class UserUpdateProfileSerializer(serializers.Serializer):
    username = serializers.CharField(
        label='username',
        write_only=True,
        required=False,

    )
    location = serializers.CharField(
        label='location',
        write_only=True,
        required=False,
    )
    things_i_love = serializers.CharField(
        label='Things I Love',
        write_only=True,
        required=False,
    )
    profile_image = serializers.CharField(
        label='Project Image',
        write_only=True,
        required=False,
    )
    description = serializers.CharField(
        label='Description',
        write_only=True,
        required=False,

    )

    def validate_email(self, value):
        try:
            return User.objects.get(
                email=value,
                is_active=False,
            )
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'You have registered with different email!'
            )

    # def validate(self, data):
    #     user = data.get('email')
    #     if type(ImageField) != type(data.get('profile_image')):
    #         raise serializers.ValidationError({
    #             'Location': 'Wrong location entered!'
    #         })
    #     return data

    def save(self, validated_data):
        user = validated_data.get('email')
        profile = Profile.objects.get(user=user)
        user.username = validated_data.get('username')
        profile.location = validated_data.get('location')
        profile.phone_number = validated_data.get('phone_number')
        profile.things_i_love = validated_data.get('things_i_love')
        profile.description = validated_data.get('description')
        profile.joined_date = validated_data.get('joined_date')
        profile.profile_image = validated_data.get('profile_image')
        return profile
