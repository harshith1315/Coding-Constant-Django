from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    qno = models.IntegerField()
    question = models.CharField(max_length=100)
    
    sinpu = models.CharField(max_length=100)
    soutpu = models.CharField(max_length=100)
    
    inpu = models.CharField(max_length=100)
    outpu = models.CharField(max_length=100)
    
    inpu2 = models.CharField(max_length=100)
    outpu2 = models.CharField(max_length=100)
    
    inpu3 = models.CharField(max_length=100)
    outpu3 = models.CharField(max_length=100)
    
    inpu4 = models.CharField(max_length=100)
    outpu4 = models.CharField(max_length=100)
    
    def __str__(self):
        return self.question
class time(models.Model):
    time = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.time
    
# models.py



class Leaderboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0)
