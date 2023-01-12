from django.db import models

class Yeast_Type(models.Model):
    yeast_type = models.CharField(max_length=50)
    ounces = models.IntegerField()
    grams = models.IntegerField()
