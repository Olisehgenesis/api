from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path(r'', include('django.contrib.auth.urls')),
]
