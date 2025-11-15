from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    
    return render(request, 'main/services.html')

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            subject = f"New Contact Form Submission from {name}"
            message_body = f"""
Name: {name}
Email: {email}
Phone: {phone}
Message:
{message}
"""

            # ✅ Safe email sending
            email_sent = True
            try:
                send_mail(
                    subject,
                    message_body,
                    settings.DEFAULT_FROM_EMAIL,
                    ['shanassociatestnj@gmail.com'],  # where you receive messages
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")  # logs the error
                email_sent = False

            # Render success page with message
            if email_sent:
                return render(request, 'main/success.html', {
                    'message': 'Your message has been sent successfully ✅'
                })
            else:
                return render(request, 'main/success.html', {
                    'message': 'Your message was received, but email delivery failed. We will contact you soon.'
                })
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

def success_view(request):
    return render(request, 'main/success.html')

def our_teams(request):
    return render(request, 'main/our_team.html')



