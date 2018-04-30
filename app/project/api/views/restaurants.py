from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers


# @route   POST api/restaurants/new/
# @desc    Post new restaurant
# @access  Public
from project.api.serializers.restaurants import RestaurantRatingSerializer
from project.api.serializers.users import UserSerializer
from project.restaurant.feed.models import Restaurant


class PostNewRestaurantView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, **kwargs):
        return Response(self.get_serializer(request.restaurant).data)

    def post(self, request, **kwargs):
        return Response(self.get_serializer(request.restaurant).data)
        serializer = self.get_serializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        restaurant = serializer.save()
        return Response(self.get_serializer(restaurant).data)


# @route   GET api/restaurants/
# @desc    Get the list of all the restaurants
# @access  Public
class GetAllRestaurantsView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        return Response(RestaurantRatingSerializer(request.user.all(), many=True).data)


# @route   GET api/restaurants/?search=<str:search_string/>
# @desc    Get the restaurant by name
# @access  Public
class GetRestaurantByNameView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, user_id):
        return Response(RestaurantRatingSerializer(Restaurant.objects.filter(user_id)).data)


# @route   GET api/restaurants/<int:category_id/>
# @desc    Get restaurants by category
# @access  Public
class GetRestaurantByCategoryView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, user_id):
        return Response(UserSerializer(User.objects.filter(user_id)).data)


# @route   GET api/restaurants/<int:user_id/>
# @desc    Get restaurants created by specific user
# @access  Public
class GetRestaurantByUserView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, user_id):
        return Response(UserSerializer(User.objects.filter(user_id)).data)


# @route   GET/POST api/restaurants/<int:id/>
# @desc    Get, update and delete a restaurant by ID
# @access  Public
class GetUpdateDeleteRestaurantByIDView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, user_id):
        return Response(UserSerializer(User.objects.filter(user_id)).data)
