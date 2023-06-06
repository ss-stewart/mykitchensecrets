from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def recipes_index(request):
  recipes = Recipe.objects.all()
  return render(request, 'recipes/index.html', {
    'recipes': recipes
  })

def recipes_detail(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  return render(request, 'recipes/detail.html', {
    'recipe': recipe
  })

class RecipeCreate(CreateView):
  model = Recipe
  fields = '__all__'

class RecipeUpdate(UpdateView):
  model = Recipe
  fields = ['title', 'ingredients', 'directions']

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes'