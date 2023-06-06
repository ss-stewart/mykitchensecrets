from django.contrib import admin
from .models import Recipe, Tool

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Tool)