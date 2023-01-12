from django.db import models

class Salt_Type(models.Model):
    salt_type = models.CharField(max_length=50)
    teaspoons = models.IntegerField()
    grams = models.IntegerField()
