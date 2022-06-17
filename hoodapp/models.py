from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE , related_name='profile')
    bio = models.TextField(max_length=300,blank =True)
    email = models.CharField(max_length=100, default = '')
    location = models.CharField(max_length=100,blank =True)
    profile_pic = models.ImageField( upload_to='profile/', blank ='true',default='default.png')
