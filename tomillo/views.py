
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

class Single(TemplateView):
    template_name = 'tomillo/single.html'

class Blog(TemplateView):
    template_name = 'tomillo/archive.html'

class Contact(TemplateView):
    template_name = 'tomillo/contact.html'


