from enum import auto
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    id=models.AutoField(primary_key=True)
    Author=models.ForeignKey(User, on_delete=models.CASCADE)
    Title=models.CharField(max_length=250)
    Body = models.TextField(max_length=500)
    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)
