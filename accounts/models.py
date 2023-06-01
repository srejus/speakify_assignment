from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Interest(models.Model):
    interest = models.CharField(max_length=100)
    
    
class UserProfile(AbstractUser):
    phone = models.CharField(max_length=15,null=True,blank=True)
    GENDER_CHOICES = (
        ('male','MALE'),
        ('female','FEMALE')
    )
    gender = models.CharField(max_length=6,null=True,choices=GENDER_CHOICES)
    country = models.CharField(max_length=100,null=True,blank=True)
    interest = models.ManyToManyField(Interest)
    is_online = models.BooleanField(default=False)
    
    
    