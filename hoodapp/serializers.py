from rest_framework import serializers
from .models import NeighbourHood, LANGUAGE_CHOICES, STYLE_CHOICES

class NeighbourHoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = NeighbourHood
        fields = ('name', 'location', 'occupants_count', 'hood_image',)














