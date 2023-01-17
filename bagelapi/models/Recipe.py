from django.db import models
from bagelapi.models import Flour_Type, Yeast_Type, Salt_Type, User

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    flour = models.ForeignKey(Flour_Type, on_delete=models.CASCADE)
    flour_amount = models.IntegerField()
    salt = models.ForeignKey(Salt_Type, on_delete=models.CASCADE)
    salt_amount = models.IntegerField()
    yeast = models.ForeignKey(Yeast_Type, on_delete=models.CASCADE)
    yeast_amount = models.IntegerField()
    water = models.IntegerField()
    directions = models.CharField(max_length=400)
    image = models.CharField(max_length=400)
    public = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def recipe_categories(self):
        return self.__recipe_categories

    @recipe_categories.setter
    def recipe_categories(self, value):
        self.__recipe_categories=value
