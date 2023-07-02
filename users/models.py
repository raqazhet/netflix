from django.db import models

class User (models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    createdAt =models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)

