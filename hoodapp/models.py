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
class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    location= models.CharField(max_length=60,null=True)
    occupants_count = models.IntegerField(null  = True ,blank = True)
    def __str__(self):
        return f'{self.name} Neighbourhood'
    def save_neighbourhood(self):
        self.save()
    def delete_neighbourhood(self):
        self.delete()
class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200,default='')
    description = models.TextField(default='')

    def save_business(self):
        self.save()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def __str__(self):
        return f'{self.name}Business' 

class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def __str__(self):
        return f'{self.title}Post'


