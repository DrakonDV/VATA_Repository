from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class testModel(models.Model):
    testText = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")  

class Object(models.Model):
    objectName = models.CharField(max_length=25)
    objectCategory = models.CharField(max_length=6)
    objectImage = models.ImageField(upload_to='VATA_mainApp\static\VATA_mainApp\ObjectImages')
    

class Place(models.Model):
    placeName = models.CharField(max_length=25)
    location = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=1000)
    placeImage = models.ImageField(upload_to='VATA_mainApp\static\VATA_mainApp\PlaceImages',blank=True, null=True)
    placeCategory = models.CharField(max_length=6)
    


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Place, on_delete=models.CASCADE)  


    class Meta:
        unique_together = ('usuario', 'lugar')

