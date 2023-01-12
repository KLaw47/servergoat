from django.db import models

class Recipe_Cat(models.Model):
    recipe_id = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    
