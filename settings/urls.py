from django.contrib import admin
from django.urls import path
from settings import views

app_name = 'settings'

urlpatterns = [
    path('configurações/', views.settings, name='settings'),
    
]