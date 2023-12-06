"""
URL configuration for yumify_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
#from yumify_django import views
#from .views import index, recipe_detail, create_recipe, like, unlike


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='recipes:index'),
    path('<int:recipe_id>', views.recipe_detail, name='recipes:recipe_detail'),
    path('create/', views.create_recipe, name='recipes:create_recipe'),
    path('like/<int:recipe_id>', views.like_recipe, name='recipes:like_recipe'),
    path('unlike/<int:recipe_id>', views.unlike_recipe, name='recipes:unlike_recipe'),
]
