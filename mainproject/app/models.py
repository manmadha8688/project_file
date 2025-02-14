from django.db import models

# Create your models here.
class destinations(models.Model):
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
class reviews(models.Model):
    ratting = models.IntegerField()
    discription = models.TextField()
