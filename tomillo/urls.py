from django.contrib import admin
from django.urls import path
from .views import *
from tomillo import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include

urlpatterns = [
    path('about_us/', AboutUs.as_view(), name = 'about_us'),
    path('partners/', Partners.as_view(), name = 'partners'),   
    path('resources/', Resources.as_view(), name = 'resources'),
    path('alumni/', Alumnis.as_view(), name = 'alumni'),
    path('press/', Press.as_view(), name = 'press'),
    path('legal/', Legal.as_view(), name = 'legal'),
    path('contact/', ContactUs.as_view(), name='contact'),
    
    path('formacion/<int:id>', Formacion.as_view(), name='formacion'),
    path('edicion/<int:id>', Edicion.as_view(), name='edicion'),
    
    path('index/', Index, name='set_language'),
    path('i18n/', include('django.conf.urls.i18n')),

 
  ]


  
   

    

  