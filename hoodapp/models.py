from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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


