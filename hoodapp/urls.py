from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [ 

    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('profile-update/',views.update_profile, name='update_profile'), 
    path('profile/<pk>/',views.profile, name = 'profile'),
    path('create-hood/',views.createhood, name='createhood'), 
    path('search/',views.search_results, name='search_results'),
    path('search_hood/',views.search_hoods, name='search_hood'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
