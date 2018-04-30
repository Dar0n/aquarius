from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from rest_framework import serializers

User = get_user_model()


# TODO modify the body of the email so it prefills the from on validation url

class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label="E-Mail address"
    )

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
            raise serializers.ValidationError(
                "User with this email address already exists."
            )
        except User.DoesNotExist:
            return value

    @staticmethod
    def send_registration_email(email, code):
        message = EmailMessage(
            subject="Luna registration",  # backend is http://aquarius.propulsion-learn.ch/backend/api/
            body=f"This is your registration link =>> http://aquarius.propulsion-learn.ch/registration/validation?code={code}&email={email}",
            to=[email],
            # here we put [] around email so that we could use
            # this for multiple user emails. Otherwise that would not work.
        )
        message.send()

    def register_user(self, email):
        new_user = User.objects.create_user(
            username=email,
            email=email,
            is_active=False
        )
        self.send_registration_email(
            email=email,
            code=new_user.user_profile.registration_code,
        )
        return new_user


class RegistrationValidationSerializer(serializers.Serializer):
    code = serializers.CharField(
        label='Validation code',
        write_only=True,
    )
    password = serializers.CharField(
        label='password',
        write_only=True,
    )
    password_repeat = serializers.CharField(
        label='password',
        write_only=True,
    )
    first_name = serializers.CharField(
        label='First name'
    )
    last_name = serializers.CharField(
        label='Last name'
    )

    def validate(self, data):
        if data.get('password') != data.get('password_repeat'):
            raise serializers.ValidationError({
                'password': 'Passwords are not equal!'
            })
        return data

    def validate_code(self, value):
        try:
            return User.objects.get(
                user_profile__registration_code=value,
                is_active=False,
            )
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'Wrong validation code or already validated!'
            )

    def save(self, validated_data):
        user = validated_data.get('code')
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.is_active = True
        user.set_password(validated_data.get('password'))
        user.save()
        return user
