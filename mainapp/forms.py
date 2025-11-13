from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    phone = forms.CharField(max_length=15, label='Phone Number', required=False)
    message = forms.CharField(widget=forms.Textarea, label='Message')
