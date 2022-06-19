from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.NeighbourHood)

