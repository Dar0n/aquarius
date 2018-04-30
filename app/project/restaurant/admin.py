from django.contrib import admin
from project.restaurant.feed.models import Review, Restaurant, ReviewLike, Comment, CommentLike

admin.site.register(Review)
admin.site.register(Restaurant)
admin.site.register(ReviewLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
