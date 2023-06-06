from django.db import models
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
  title = models.CharField(max_length=100)
  ingredients = models.TextField()
  directions = models.TextField()

  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'recipe_id': self.id})
