from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from project.api.helpers import code_generator


class Profile(models.Model):
    user = models.OneToOneField(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_profile"
    )
    location = models.CharField(
        verbose_name="location",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="location"
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )
    things_i_love = models.TextField(
        verbose_name="things_i_love",
        default='',
        blank=True,
    )
    description = models.TextField(
        verbose_name="description"
    )
    joined_date = models.DateField()
    profile_image = models.ImageField(
        upload_to='profile_image',
        blank=True,
    )

    def __str__(self):
        return self.user.username

    registration_code = models.CharField(
        verbose_name="registration code",
        max_length=15,
        unique=True,
        default=code_generator,
    )

    def generate_new_code(self):
        while True:
            code = code_generator()
            if Profile.objects.filter(registration_code=code):
                continue
            break
        self.registration_code = code
        self.save()
