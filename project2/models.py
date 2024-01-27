from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=100)
    email = models.EmailField()
    
    ROLE_CHOICES = {
        "AD": "admin",
        "US": "user"
    }
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default="user")

