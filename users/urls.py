from django.urls import include, path
from . import views

urlpatterns = [
    path('getusers', views.get_users),
    path('adduser', views.add_user),
    ]