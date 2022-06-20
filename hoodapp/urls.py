from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [ 

    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('profile-update/',views.update_profile, name='update_profile'), 
    path('profile/<pk>/',views.profile, name = 'profile'),
    path('create-hood/',views.createhood, name='createhood'), 
    path('search/',views.search_results, name='search_results'),
    path('about/', views.about, name='about'),
    path('hoods/', views.NeighbourhoodList.as_view(), name ='hoods-list'),
    path('hoods/<int:pk>/', views.NeighbourhoodDetail.as_view(),name ='hoods-detail'),
    path('business/', views.BusinessList.as_view(),name ='business-list'),
    path('business/<int:pk>/', views.BusinessDetail.as_view(),name ='business-detail'),
    path('posts/', views.PostList.as_view(),name ='posts-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(),name ='posts-detail'),
    path('logout/', auth_views.logout_then_login, name='logout'),


]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
