from django.contrib import admin
from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.landing_page, name='main'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('contato/', views.contact, name='contato'),
    path('sobre/', views.about, name='sobre'),
]