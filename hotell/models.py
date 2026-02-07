from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    numTel = models.CharField(max_length=40)
    prixNuit = models.CharField(max_length=50)
    devise = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.name