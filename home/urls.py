from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.landing_page),
    path('home/', views.home),
    path('login/', views.login),
    path('contato/', views.contact),
    path('sobre/', views.about),
]