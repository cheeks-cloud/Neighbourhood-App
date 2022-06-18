from django import forms
from django.contrib.auth.models import User
from .models import *

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('admin',)

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']
        
