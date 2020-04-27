from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            self.fields['contact_name'].label = "Your name:"
            self.fields['contact_email'].label = "Your email:"
            self.fields['subject'].label = "Subject"
            self.fields['message'].label = "Message"

