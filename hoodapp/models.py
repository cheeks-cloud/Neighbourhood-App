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

    def __str__(self) -> str:
        return f'{self.name}Business'
