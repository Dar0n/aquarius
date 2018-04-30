from django.contrib.auth import get_user_model
from rest_framework import serializers

from project.restaurant.feed.models import Comment

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created', 'modified', 'review', 'user']
        read_only_fields = ['id', 'modified', 'created','review', 'user']


    def create(self, validated_data):
        return Comment.objects.create(
            **validated_data,
            review=self.context.get('review'),
            user=self.context.get('request').user,
        )
