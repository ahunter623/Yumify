from django.shortcuts import render

from .models import Recipe, Ingredient, Like
from django.contrib.auth.decorators import login_required

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    likes = Like.objects.filter(recipe=recipe)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients, 'likes': likes})

@login_required
def create_recipe(request):
    if request.method == 'POST':
        recipe = Recipe()
        recipe.name = request.POST['name']
        recipe.description = request.POST['description']
        recipe.author = request.user
        if request.FILES['image']:
            recipe.image = request.FILES['image']
        recipe.save()

        ingredients = request.POST.getlist('ingredients')
        for ingredient in ingredients:
            Ingredient.objects.create(recipe=recipe, name=ingredient)

        return redirect('recipes:index')
    else:
        return render(request, 'recipes/create_recipe.html')

@login_required
def like_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    Like.objects.create(recipe=recipe, user=request.user)
    return redirect('recipes:recipe_detail', recipe_id=recipe_id)

@login_required
def unlike_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    Like.objects.filter(recipe=recipe, user=request.user).delete()
    return redirect('recipes:recipe_detail', recipe_id=recipe_id)
