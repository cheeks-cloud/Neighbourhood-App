"""hoodproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views 
from hoodapp import views
from django.conf.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('index/',views.index, name='index'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile-update/',views.update_profile, name='update_profile'),
    path('accounts/profile/', auth_views.LoginView.as_view(template_name='profile.html')),
    path('profile/<pk>/',views.profile, name = 'profile'),
    path('create-hood/',views.createhood, name='createhood'), 
    path('hood/<id>/',views.neighbourhood, name = 'neighbourhood'),
    path('join_neighbourhood/<id>/', views.join_neighbourhood, name='join-neighbourhood'),
    path('business/<id>/',views.createbusiness, name = 'create-business'),
    path('post/<hood_id>/',views.post, name = 'post'),
    path('change_neighbourhood/<id>/', views.change_neighbourhood, name='change-neighbourhood'),
    path('search/',views.search_results, name='search_results'),
    path('api/', include('rest_framework.urls')),
    path('', include('hoodapp.urls')),
    path('logout/', auth_views.logout_then_login, name='logout'),
]
