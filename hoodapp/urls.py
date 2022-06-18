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
 

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
