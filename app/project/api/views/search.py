from django.db.models import Q
from rest_framework.generics import ListAPIView
from project.api.serializers.users import UserSerializer
from project.restaurant.feed.models import Restaurant


# @route   GET api/search
# @desc    Get the review, restaurant or user profile
# @access  Public
class SearchListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = Restaurant.objects.all()

    def filter_queryset(self, queryset):
        search_string = self.request.query_params.get('search')
        if search_string:
            queryset = queryset.filter(
                Q(username__contains=search_string) |
                Q(restaurant__contains=search_string) |
                Q(review__contain=search_string)
            )
        return queryset
