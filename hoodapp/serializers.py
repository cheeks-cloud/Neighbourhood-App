from rest_framework import serializers
from .models import NeighbourHood, Business,Post,LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class NeighbourHoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = NeighbourHood
        fields = ('name', 'location', 'occupants_count', 'image','admin')

class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = ('name', 'phone_no', 'email', 'description','neighbourhood')

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'image', 'info', 'post_date','neighbourhood','user')











