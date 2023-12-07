from django.contrib import admin

from .models import Profile, Post, LikePost, FollowersCount

admin.site.register(Profile)
admin.site.register(Post)
#admin.site.register(Recipe)
#admin.site.register(Ingredient)

admin.site.register(LikePost)
#admin.site.register(Comment)
admin.site.register(FollowersCount)