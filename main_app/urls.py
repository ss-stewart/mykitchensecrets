from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('recipes/', views.recipes_index, name='index'),
  path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
  path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
  path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
  path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
  path('recipes/<int:recipe_id>/assoc_tool/<int:tool_id>/', views.assoc_tool, name='assoc_tool'),
  path('recipes/<int:recipe_id>/unassoc_tool/<int:tool_id>/', views.unassoc_tool, name='unassoc_tool'),
  path('tools/', views.ToolList.as_view(), name='tools_index'),
  path('tools/<int:pk>/', views.ToolDetail.as_view(), name='tools_detail'),
  path('tools/create/', views.ToolCreate.as_view(), name='tools_create'),
  path('tools/<int:pk>/update/', views.ToolUpdate.as_view(), name='tools_update'),
  path('tools/<int:pk>/delete/', views.ToolDelete.as_view(), name='tools_delete'),
  path('accounts/signup/', views.signup, name='signup')
]