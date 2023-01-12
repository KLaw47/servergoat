from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=400)
    uid = models.CharField
