from django.urls import path
from . import views

urlpatterns = [
     path('businesses/<id>', views.businesses, name='businesses'),
     path('new_business/', views.new_business, name='new_business'),
]
