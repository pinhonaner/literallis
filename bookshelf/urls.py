from django.contrib import admin
from django.urls import path
from bookshelf import views

app_name = 'bookshelf'

urlpatterns = [
    path('prateleira/', views.bookshelf, name='bookshelf'),
    path('', views.book, name='book' ),
]