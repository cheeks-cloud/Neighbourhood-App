from django import forms
from django.contrib.auth.models import User
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user') 