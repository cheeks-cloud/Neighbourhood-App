from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 

  path("register", views.register_request, name="register"),
  path("login", views.login_request, name="login"),
  path("logout", views.logout_request, name= "logout"),
  path("profile/", views.profile, name="profile"),
  path("profile/update/", views.update_profile, name="update_profile"),
  path('businesses/<id>', views.businesses, name='businesses'),
  path('new_business/', views.new_business, name='new_business'),
  path('about/', views.about, name='about'),
  path('hoods', views.NeighbourhoodList.as_view(), name ='hoods-list'),
  path('hoods/<int:pk>/', views.NeighbourhoodDetail.as_view(),name ='hoods-detail'),
  path('business', views.BusinessList.as_view(),name ='business-list'),
  path('business/<int:pk>/', views.BusinessDetail.as_view(),name ='business-detail'),
  path('posts', views.PostList.as_view(),name ='posts-list'),
  path('posts/<int:pk>/', views.PostDetail.as_view(),name ='posts-detail'),


]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
