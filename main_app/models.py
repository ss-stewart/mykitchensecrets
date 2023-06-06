from json import tool
from django.db import models
from django.urls import reverse

# Create your models here.
class Tool(models.Model):
  name = models.CharField(max_length=50)
  cost = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('tools_detail', kwargs={'pk': self.id})

class Recipe(models.Model):
  title = models.CharField(max_length=100)
  ingredients = models.TextField()
  directions = models.TextField()
  # Create a M:M relationship with Tool
  # tools is the Related Manager
  tools = models.ManyToManyField(Tool)

  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'recipe_id': self.id})