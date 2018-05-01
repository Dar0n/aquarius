from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from project.api.views.categories import GetCategoriesView
from project.api.views.registration import RegistrationView, RegistrationValidationView
#
from project.api.views.password_reset import PasswordResetView, PasswordResetValidationView
from project.api.views.reviews import RestaurantReviewsView, ReviewCreateView, ReviewByUserView, \
    GetPostDeleteReviewView, ReviewLikeDislikeView, LikedReviewsView, CommentedReviewsView

# from project.api.views.feed import FeedDisplayView, UserGetAllPosts, PostFromFollowingsView, ListFriendsPostsView
# from project.api.views.posts import PostGetUpdateDeleteView, PostCreateView, PostThatUserLiked, PostLikeDislikeView, \
#     ShareAPostView
# from project.api.views.users import ProfileFollowUnfollowAUser, ProfileFollowingUsersView, ProfileFollowerUsersView, \
#     AllUsersView, GetUserProfile, UserFriendRequests, SendFriendRequestView, PendingFriendRequestsView, \
#     AcceptFriendRequestView, RejectFriendRequestView, ListAllFriendsView, UnfriendAFriendsView, UserProfileView

app_name = "api"

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("registration/validation/", RegistrationValidationView.as_view(), name="registration-validation"),
    path("auth/password-reset/", PasswordResetView.as_view(), name="password-reset"),
    path("auth/password-reset/validate/", PasswordResetValidationView.as_view(), name="password-reset-validation"),
    path("reviews/restaurant/<int:restaurant_id>/", RestaurantReviewsView.as_view(), name="restaurant-reviews"),
    path("reviews/new_review/<int:pk>/", ReviewCreateView.as_view(), name="create-review"),
    path("reviews/user/<int:user_id>/", ReviewByUserView.as_view(), name="show-reviews-for-user"),
    path("reviews/<int:review_id>/", GetPostDeleteReviewView.as_view(), name="get-post-delete-review"),
    path("reviews/like/<int:review_id>/", ReviewLikeDislikeView.as_view(), name="like-dislike-review"),
    path("reviews/likes/", LikedReviewsView.as_view(), name="liked-reviews"),
    path("reviews/comments/", CommentedReviewsView.as_view(), name="commented-reviews"),
    path("category/list/", GetCategoriesView.as_view(), name='get-list-of-categories'),
    # path("<int:user_id>/followers/", ProfileFollowerUsersView.as_view(), name="followers"),
    # path("users/", AllUsersView.as_view(), name="list-all-users"),
    # path("users/<int:user_id>/", GetUserProfile.as_view(), name="get-user-profile"),
    # path("users/friendrequests/", UserFriendRequests.as_view(), name="get-user-friend-requests"),
    # path("users/friendrequests/<int:user_id>/", SendFriendRequestView.as_view(), name="send-friend-request"),
    # path("users/friendrequests/pending/", PendingFriendRequestsView.as_view(), name="pending-friend-requests"),
    # path("users/friendrequests/accept/<int:request_id>/", AcceptFriendRequestView.as_view(),
    #      name="accept-friend-request"),
    # path("users/friendrequests/reject/<int:request_id>/", RejectFriendRequestView.as_view(),
    #      name="reject-friend-request"),
    # path("users/friends/", ListAllFriendsView.as_view(), name="list-all-friends"),
    # path("users/friends/unfriend/<int:user_id>/", UnfriendAFriendsView.as_view(), name="unfriend-a-friend"),
    # path("me/", UserProfileView.as_view(), name="show-update-userprofile"),
]
