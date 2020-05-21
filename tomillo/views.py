from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView
from django.contrib.auth.models import User
from .forms import ContactForm
from django.core.mail import send_mail
from django.utils import translation
from django.utils.translation import gettext
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse

class Inicio(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = 'index.html'
    success_url = reverse_lazy('inicio')
    success_message = "Your message has been successfully sent. Thank you for contacting us."
    

    def form_valid(self, form):
        contact_name = form.cleaned_data['contact_name']
        contact_email = form.cleaned_data['contact_email']
        subject = form.cleaned_data['subject']
        message = "{0} has sent you a new message:\n\n{1}".format(contact_name, form.cleaned_data['message'])
        send_mail(subject, message, contact_email, ['gotech@alwaysdata.net'], fail_silently = False)
        return super(Inicio, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context['aliado'] = Aliado.objects.all()
        context['numero'] = Numero.objects.all()
        context['prensa'] = Prensa.objects.all()
        context['programas'] = Programa.objects.all()
        context['promociones'] = Promocion.objects.all()
        context['testimonio'] = Publicacion.objects.all().order_by('-id')[:3]
        return context

class Template(ListView):
    template_name = 'tomillo/template.html'     

    def get_context_data(self, **kwargs):
        context = super(Template, self).get_context_data(**kwargs)
        context['programas'] = Programa.objects.all()
        context['promociones'] = Promocion.objects.all()
        return context


class Formacion(ListView):
    model = Programa
    template_name = 'tomillo/programa.html'
    context_object_name = 'programas'
    queryset = Programa.objects.all()

                
    def get_context_data(self, **kwargs):
        context=super(Formacion, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('id', None)
        context['promociones']=Promocion.objects.all() 
        context['formacionId']=Programa.objects.filter(id=parametro)
        return context

class AboutUs(ListView):
    model = Programa
    template_name = 'tomillo/aboutUs.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        context['programas'] = Programa.objects.all()
        context['promociones'] = Promocion.objects.all()
        return context

class Partners(ListView):
    model = Aliado
    template_name = 'tomillo/partners.html'
    context_object_name = 'aliado'
    queryset = Aliado.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Partners, self).get_context_data(**kwargs)
        context['programas'] = Programa.objects.all()
        context['promociones'] = Promocion.objects.all()
        return context

class Blog(TemplateView):
    template_name = 'tomillo/archive.html'

class ContactUs(SuccessMessageMixin, FormView):
    form_class = ContactForm
    success_url = reverse_lazy('tomillo:contact')
    template_name = 'tomillo/contact.html'
    success_message = "Your message has been successfully sent. Thank you for contacting us."
    
    def form_valid(self, form):
        contact_name = form.cleaned_data['contact_name']
        contact_email = form.cleaned_data['contact_email']
        subject = form.cleaned_data['subject']
        message = "{0} has sent you a new message:\n\n{1}".format(contact_name, form.cleaned_data['message'])
        send_mail(subject, message, contact_email, ['gotech@alwaysdata.net'], fail_silently = False)
        return super(ContactUs, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactUs, self).get_context_data(**kwargs)
        context['programas'] = Programa.objects.all()
        context['promociones'] = Promocion.objects.all()
        return context
            
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

class Resources(ListView):
    paginate_by = 8
    model = Recurso
    template_name = 'tomillo/resources.html'
    context_object_name= 'res' 
    queryset = Recurso.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(Resources, self).get_context_data(**kwargs)
        context['programas'] = Programa.objects.all()
        context['promociones'] = Promocion.objects.all()
        return context
    
class Alumnis(ListView):
    model = Alumni
    template_name = 'tomillo/alumni.html'
    context_object_name = 'alumni'
    queryset = Alumni.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Alumnis, self).get_context_data(**kwargs)
        context['programas'] = Programa.objects.all()
        context['promociones'] = Promocion.objects.all()
        return context
    
class Legal(TemplateView):
    template_name = 'tomillo/legal.html'

    def get_context_data(self, **kwargs):
        context = super(Legal, self).get_context_data(**kwargs)
        context['programas'] = Programa.objects.all()
        context['promociones'] = Promocion.objects.all()
        return context

class Press(ListView):
    paginate_by = 3
    model = Prensa
    template_name = 'tomillo/press.html'
    context_object_name = 'prensa'
    queryset = Prensa.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(Press, self).get_context_data(**kwargs)
        context['programas'] = Programa.objects.all()
        context['promociones'] = Promocion.objects.all()
        return context


def Index(request):
    return render(request,'tomillo/template.html')
    

   




