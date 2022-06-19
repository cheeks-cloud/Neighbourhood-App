from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



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



