from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('singup', views.handleSignup, name='singup'),
    path('login', views.handleLogin, name='login'),
    path('logout', views.handleLogout, name='logout'),

]