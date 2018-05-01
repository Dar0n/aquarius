from rest_framework import serializers

from project.restaurant.feed.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "content", "created", "modified", "user", "rating", "restaurant", "comment", "review_likes"]
        # this field cannot be changed. Alternatively, we could update
        # the date if we update the post, then this wouldn't be here
        read_only_fields = ["id", "user", "created", "modified", "restaurant"]

    def create(self, validated_data):
        return Review.objects.create(
            # **validated_data,
            content=validated_data.get("content"),
            rating=validated_data.get("rating"),
            restaurant=self.context.get("restaurant"),
            # alternative way to pass all the fields is to use
            # just **validated_data
            user=self.context.get("request").user,
        )
