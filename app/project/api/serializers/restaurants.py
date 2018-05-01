from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.restaurant.models import Restaurant

User = get_user_model()


class RestaurantRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "user"]
        read_only_fields = fields
