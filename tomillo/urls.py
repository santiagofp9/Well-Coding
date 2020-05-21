from django.contrib import admin
from django.urls import path
from .views import *
from tomillo import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include

urlpatterns = [
    path('about_us/', AboutUs.as_view(), name = 'about_us'),
    path('partners/', Partners.as_view(), name = 'partners'),
    path('blog/', Blog.as_view(), name = 'blog'),
    path('f5/', TomilloF5.as_view(), name = 'f5'),
    path('graduation2020/', Promo2020.as_view(), name = 'promo2020'),
    path('cybersecurity/', Cybersecurity.as_view(), name = 'cybersecurity'),
    path('formal_education/', FormalEducation.as_view(), name = 'formal_education'),
    path('ele_eco/', EleEco.as_view(), name = 'ele_eco'),
    path('adm/', Adm.as_view(), name = 'adm'),
    path('computing/', Computing.as_view(), name = 'computing'),
    path('networks/', Networks.as_view(), name = 'networks'),
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


  
   

    

  