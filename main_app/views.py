from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe, Tool

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
  # First, create a list of the tool ids that the recipe has
  id_list = recipe.tools.all().values_list('id')
  # Query for the tools that the recipe doesn't have
  # by using the exclude() method vs. the filter() method
  tools_recipe_doesnt_have = Tool.objects.exclude(id__in=id_list)
  return render(request, 'recipes/detail.html', {
    'recipe': recipe,
    'tools': tools_recipe_doesnt_have
  })

class RecipeCreate(CreateView):
  model = Recipe
  fields = ['title', 'ingredients', 'directions']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RecipeUpdate(UpdateView):
  model = Recipe
  fields = ['title', 'ingredients', 'directions']

class RecipeDelete(DeleteView):
  model = Recipe
  success_url = '/recipes'
  
class ToolList(ListView):
  model = Tool

class ToolDetail(DetailView):
  model = Tool

class ToolCreate(CreateView):
  model = Tool
  fields = '__all__'

class ToolUpdate(UpdateView):
  model = Tool
  fields = ['name', 'cost']

class ToolDelete(DeleteView):
  model = Tool
  success_url = '/tools'

def assoc_tool(request, recipe_id, tool_id):
  Recipe.objects.get(id=recipe_id).tools.add(tool_id)
  return redirect('detail', recipe_id=recipe_id)

def unassoc_tool(request, recipe_id, tool_id):
  Recipe.objects.get(id=recipe_id).tools.remove(tool_id)
  return redirect('detail', recipe_id=recipe_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message }
  return render(request, 'registration/signup.html', context)
  
  