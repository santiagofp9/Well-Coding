
from django.shortcuts import render,redirect
from .models import *




from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
#from .forms import UserForm,FormularioLogin,CestaForm,UserCreationForm
from django.views.generic.edit import CreateView,FormView


class Inicio(TemplateView):
    template_name = 'index.html'

class AboutUs(TemplateView):
    template_name = 'tomillo/aboutUs.html'

class Partners(TemplateView):
    template_name = 'tomillo/partners.html'

class Blog(TemplateView):
    template_name = 'tomillo/archive.html'

class Contact(TemplateView):
    template_name = 'tomillo/contact.html'

class TomilloF5(TemplateView):
    template_name = 'tomillo/f5.html'

class Promo2020(TemplateView):
    template_name = 'tomillo/promo2020.html'

class Cybersecurity(TemplateView):
    template_name = 'tomillo/cyber.html'

class FormalEducation(TemplateView):
    template_name = 'tomillo/formalEducation.html'

class EleEco(TemplateView):
    template_name = 'tomillo/ele_eco.html'

class Adm(TemplateView):
    template_name = 'tomillo/adm.html'

class Computing(TemplateView):
    template_name = 'tomillo/computing.html'

class Networks(TemplateView):
    template_name = 'tomillo/networks.html'

class NonFormalEducation(TemplateView):
    template_name = 'tomillo/nonformalEducation.html'

class Resources(TemplateView):
    template_name = 'tomillo/resources.html'
    
class Alumnis(TemplateView):
    template_name = 'tomillo/alumni.html'
    
class Legal(TemplateView):
    template_name = 'tomillo/legal.html'


class Press(ListView):
    model = Prensa
    template_name = 'tomillo/press.html'
    context_object_name = 'prensa'
    queryset = Prensa.objects.all()

   


