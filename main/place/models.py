from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField() 
    #必要なものを後で追加

class Placecomment(models.Model):
    body = models.TextField()
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    #必要なものを後で追加