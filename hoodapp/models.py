from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


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

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):

        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

class Business(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=120,default='')
    email = models.CharField(max_length=200,default='')
    description = models.TextField(default='')
    hood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)

    def save_business(self):
        self.save()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def hoods_business(cls, id):
        hoodbusiness = Business.objects.filter(hood = id)
        return hoodbusiness

    def __str__(self):
        return f'{self.name} Business' 

class Post(models.Model):
    title = models.CharField(max_length=200)
    post_image=CloudinaryField('post_image',null=True)
    post = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,default='',related_name='owner')
    hood = models.ForeignKey("Neighbourhood", on_delete=models.CASCADE,default='',related_name='neighbourhood_post')
    date_posted = models.DateField(auto_now_add=True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def hood_news(cls,id):
        hoodnews = Post.objects.filter(hood = id)
        return hoodnews

    def __str__(self):
        return f'{self.title} Post'



