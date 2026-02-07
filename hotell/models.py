from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    numTel = models.CharField(max_length=40)
    prixNuit = models.CharField(max_length=50)
    devise = models.CharField(max_length=200)
    image = CloudinaryField('image')


    def __str__(self):
        return self.name