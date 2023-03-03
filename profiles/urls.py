from django.contrib import admin
from django.urls import path
from profiles import views

app_name = 'home'

urlpatterns = [
    path('', views.profile_page, name='main'),
]