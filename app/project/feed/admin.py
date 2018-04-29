from django.contrib import admin
from .models import Review, Restaurant, Profile, ReviewLike, Comment, CommentLike

admin.site.register(Review)
admin.site.register(Restaurant)
admin.site.register(Profile)
admin.site.register(ReviewLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
