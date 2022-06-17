from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE , related_name='profile')
    bio = models.TextField(max_length=300,blank =True)
    email = models.CharField(max_length=100, default = '')
    location = models.CharField(max_length=100,blank =True)
    profile_pic = models.ImageField( upload_to='profile/', blank ='true',default='default.png')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    def delete_user(self):
        self.delete()


class Hood(models.Model):
    name = models.CharField(max_length=50)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')

