from django.db import models
import uuid

from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)       
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=120)           
    price       = models.IntegerField()                       
    description = models.TextField()                          
    thumbnail   = models.URLField()                           
    category    = models.CharField(max_length=50)             
    is_featured = models.BooleanField(default=False)   

    # tambahan KickMart
    stock       = models.PositiveIntegerField(default=0)
    brand       = models.CharField(max_length=50, blank=True)
    rating      = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    size        = models.CharField(max_length=10, blank=True) # S/M/L/41-45
    color       = models.CharField(max_length=30, blank=True)
    league      = models.CharField(max_length=40, blank=True) # EPL/LaLiga
    club        = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name