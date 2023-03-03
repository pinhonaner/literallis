from django.contrib import admin
from django.urls import path
from profiles import views

app_name = 'profile'

urlpatterns = [
    path('perfil/', views.profile_page, name='profile'),
]