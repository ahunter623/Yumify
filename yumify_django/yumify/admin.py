from django.contrib import admin

from .models import Recipe, Ingredient, Like, Comment

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Like)
admin.site.register(Comment)