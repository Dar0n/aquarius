from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from project.api.views.comments import CreateCommentOnReviewView, DeleteCommentOnReviewView, \
    LikeRemoveLikeCommentOnReviewView
from project.api.views.registration import RegistrationView, RegistrationValidationView
#
# from project.api.views.auth import PasswordResetView, PasswordResetValidationView
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

    path("review/comment/new/<int:pk>/", CreateCommentOnReviewView.as_view(), name="comment-on-review"),
    path("review/comment/<int:pk>/", DeleteCommentOnReviewView.as_view(), name="delete-comment-on-review"),
    path("review/comment/like/<int:pk>/", LikeRemoveLikeCommentOnReviewView.as_view(), name="like-comment"),
    path("review/comment/like/<int:pk>/", LikeRemoveLikeCommentOnReviewView.as_view(), name="delete-comment-on-review"),

    # path("review/comment/<int:pk>/", AllCommentsFromSingleUser.as_view(), name="comment-from-user")\
    # path("auth/password-reset/", PasswordResetView.as_view(), name="password-reset"),
    # path("auth/password-reset/validate/", PasswordResetValidationView.as_view(), name="password-reset-validation"),
    # path("feed/", FeedDisplayView.as_view(), name="feed_display"),
    # path("feed/<int:user_id>/", UserGetAllPosts.as_view(), name="user-all-posts"),
    # path("feed/followings/", PostFromFollowingsView.as_view(), name="all-posts-from-followers"),
    # path("feed/friends/", ListFriendsPostsView.as_view(), name="list-friends"),
    # path("posts/<int:post_id>/", PostGetUpdateDeleteView.as_view(), name="post_detail"),
    # path("posts/new-post/", PostCreateView.as_view(), name="post-create"),
    # path("posts/likes/", PostThatUserLiked.as_view(), name="liked-posts"),
    # path("posts/like/<int:post_id>/", PostLikeDislikeView.as_view(), name="like-dislike-a-post"),
    # path("posts/share-post/<int:post_id>/", ShareAPostView.as_view(), name="share-a-post"),
    # path("users/follow/<int:user_id>/", ProfileFollowUnfollowAUser.as_view(), name="follow-a-user"),
    # path("<int:user_id>/following/", ProfileFollowingUsersView.as_view(), name="following-users"),
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

