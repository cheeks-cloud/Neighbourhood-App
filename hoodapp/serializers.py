from rest_framework import serializers
from .models import NeighbourHood, Business,Post,LANGUAGE_CHOICES, STYLE_CHOICES

class NeighbourHoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = NeighbourHood
        fields = ('name', 'location', 'occupants_count', 'hood_image','admin')

class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = ('name', 'category', 'email', 'description','hood')

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'post_image', 'post', 'date_posted','hood','user')













