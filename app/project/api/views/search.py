from django.db.models import Q
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model

User = get_user_model()


# @route   GET api/search
# @desc    Get the review, restaurant or user profile
# @access  Public
class SearchListView(ListAPIView):

    def filter_queryset(self, queryset):
        search_string = self.request.query_params.get('search')
        if search_string:
            queryset = queryset.filter(
                Q(username__contains=search_string) |
                Q(email__contains=search_string) |
                Q(first_name__contains=search_string) |
                Q(laster_name__contains=search_string)
            )
        return queryset
