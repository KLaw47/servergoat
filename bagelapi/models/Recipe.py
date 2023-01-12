from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    flour_id = models.ForeignKey("Flour_Types", on_delete=models.CASCADE)
    flour_amount = models.IntegerField()
    salt_id = models.ForeignKey("Salt_Types", on_delete=models.CASCADE)
    salt_amount = models.IntegerField()
    yeast_id = models.ForeignKey("Yeast_Types", on_delete=models.CASCADE)
    yeast_amount = models.IntegerField()
    water = models.IntegerField()
    directions = models.CharField(max_length=400)
    image = models.CharField(max_length=400)
    public = models.BooleanField
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE)
