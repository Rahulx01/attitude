from statistics import mode
from django.db import models

# Create your models here.

class Host(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    city = models.TextField()
    print("yeah boi")

def __str__(self):
    return self.name


    
