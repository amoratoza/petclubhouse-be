from django.db import models
from .user     import User

class Pet(models.Model):
    id    = models.AutoField(primary_key=True)
    user  = models.ForeignKey(User, related_name='pet', on_delete=models.CASCADE)
    name  = models.CharField(max_length=25)
    breed = models.CharField(max_length=25)
    age   = models.IntegerField()
