from django.db import models
from django.utils import timezone

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    role = models.CharField(max_length=30)
    age = models.IntegerField()

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100) 

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=30)
    
    def __str__(self):
     return f"{self.name} - ${self.price} ({self.category})"
