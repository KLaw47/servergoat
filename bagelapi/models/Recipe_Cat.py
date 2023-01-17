from django.db import models
from bagelapi.models import Recipe, Category

class Recipe_Cat(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
