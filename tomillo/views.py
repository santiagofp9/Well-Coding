from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView
from django.contrib.auth.models import User
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse

class Inicio(TemplateView):
    template_name = 'index.html'

class AboutUs(TemplateView):
    template_name = 'tomillo/aboutUs.html'

class Partners(TemplateView):
    template_name = 'tomillo/partners.html'

class Blog(TemplateView):
    template_name = 'tomillo/archive.html'

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            # contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, contact_email, ['alyona.saenco@gmail.com'])
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'tomillo/contact.html', {'form': form})

"""class ContactUs(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('tomillo:contact')
    template_name = 'tomillo/contact.html'
    
    def form_valid(self, form):
        contact_name = form.cleaned_data['contact_name']
        contact_email = form.cleaned_data['contact_email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        template = get_template('tomillo/content_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'subject': subject,
            'message': message,
        }

        content = template.render(context)

        email = EmailMessage(
            'New contact form submission',
            content,
            'Your website ' + '',
            ['alyona.saenco@gmail.com'],
            headers = {'Reply-To': contact_email}
        )
        email.send()
        return super(ContactUs, self).form_valid(form)"""
            
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

   

