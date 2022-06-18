from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    location= models.CharField(max_length=60,null=True)
    occupants_count = models.IntegerField(null  = True ,blank = True)
    hood_image=CloudinaryField('hood_image',null=True)


    def __str__(self):
        return f'{self.name} NeighbourHood'

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE , related_name='profile')
    bio = models.TextField(max_length=300,blank =True)
    email = models.CharField(max_length=100, default = '')
    location = models.CharField(max_length=100,blank =True)
    profile_pic=CloudinaryField('profile_pic',null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    def delete_user(self):
        self.delete()






