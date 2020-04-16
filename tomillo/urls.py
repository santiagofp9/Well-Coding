from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Inicio.as_view(), name = 'inicio'),
    path('about_us/', AboutUs.as_view(), name = 'about_us'),
    path('partners/', Partners.as_view(), name = 'partners'),
    path('blog/', Blog.as_view(), name = 'blog'),
    path('contact/', Contact.as_view(), name = 'contact'),
    path('f5/', TomilloF5.as_view(), name = 'f5'),
    path('cybersecurity/', Cybersecurity.as_view(), name = 'cybersecurity'),
    path('formal_education/', FormalEducation.as_view(), name = 'formal_education'),
    path('non_formal_education/', NonFormalEducation.as_view(), name = 'non_formal_education'),
    path('resources/', Resources.as_view(), name = 'resources'),
    path('alumni/', Alumnis.as_view(), name = 'alumni'),
    path('press/', Press.as_view(), name = 'press'),
    path('legal/', Legal.as_view(), name = 'legal'),
  ]