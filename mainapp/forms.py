from django import forms
from .models import Contact
from django.core.validators import RegexValidator

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    phone = forms.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^[0-9]+$',
                message='Phone number must contain digits only.'
            )
            ],
            widget=forms.TextInput(attrs={
                'placeholder': 'Enter phone number',
                'pattern': '[0-9]+',
                'title': 'Only numbers allowed'
            })
    )
    message = forms.CharField(widget=forms.Textarea, label='Message')
