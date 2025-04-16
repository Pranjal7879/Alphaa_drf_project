from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    role = models.CharField(max_length=30)
    age = models.IntegerField()
