from django import forms
from django.contrib.auth.models import User
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['image','name','email','phone_no'] 


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','info','image']  

class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields=['name','location','description','image','health_center','health_email','health_contact'] 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_pic','bio','email','phone_no'] 



