from django import forms
from django.forms import TextInput

class ContactForm(forms.Form):
    contact_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name'}), required=True)
    contact_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}), required=True)
