from django.db import models
import uuid

from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=120)           
    price       = models.IntegerField()                       
    description = models.TextField()                          
    thumbnail   = models.URLField()                           
    category    = models.CharField(max_length=50)             
    is_featured = models.BooleanField(default=False)   

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)       

    # tambahan KickMart
    stock       = models.PositiveIntegerField(default=0)
    brand       = models.CharField(max_length=50, blank=True)
    rating      = models.FloatField(default=0.0)              # 0–5
    size        = models.CharField(max_length=10, blank=True) # S/M/L/41-45
    color       = models.CharField(max_length=30, blank=True)
    league      = models.CharField(max_length=40, blank=True) # EPL/LaLiga
    club        = models.CharField(max_length=60, blank=True)

# class Employe(models.Model):
#     name = models.CharField (max_length= 225)
#     age = models.IntegerField()
#     persona = models.TextField()

    def __str__(self):
        return f"{self.name} (Rp{self.price})"
