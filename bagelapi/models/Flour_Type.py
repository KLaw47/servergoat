from django.db import models

class Flour_Type(models.Model):
    flour_type = models.CharField(max_length=50)
    cups = models.IntegerField()
    grams = models.IntegerField()
