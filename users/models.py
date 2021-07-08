from django.db import models
from django.conf import settings


#my_models
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=16)
    email= models.EmailField(max_length=200)
    phone= models.CharField(max_length=10)
    class_level = models.CharField(max_length=100)
    user_type = models.CharField(max_length=30)
def __str__(self):
    return self.name
