from django.contrib import admin

from .models import Profile, Post, Recipe, Ingredient, Like, Comment, FollowersCount

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Recipe)
admin.site.register(Ingredient)

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(FollowersCount)