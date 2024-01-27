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


class Task(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    
    STATUS_CHOICES = {
        "IP": "in progress",
        "D": "done",
        "A": "assigned" 
    }
    status = models.CharField(max_length=31, choices=STATUS_CHOICES)
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    
    
    

