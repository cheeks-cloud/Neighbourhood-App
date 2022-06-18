from django import forms
from django.contrib.auth.forms import UserCreationFor
from django.contrib.auth.models import User
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',) 

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'location', 'email']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']
        

