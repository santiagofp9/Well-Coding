from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',Inicio.as_view(), name = 'inicio'),
    path('single/',Single.as_view(), name = 'single'),
    path('blog/',Blog.as_view(), name = 'blog'),
    path('contact/',Contact.as_view(), name = 'contact'),
  ]