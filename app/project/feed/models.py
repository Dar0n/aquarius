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

