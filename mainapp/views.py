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

            # send email to your chosen admin/company mail
            send_mail(
                subject,
                message_body,
                settings.DEFAULT_FROM_EMAIL,
                ['shanassociatestnj@gmail.com'],  # 📩 where you want to receive messages
                fail_silently=False,
            )

            return redirect('success')  # create a success page or message
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def success_view(request):
    return render(request, 'main/success.html')

def our_teams(request):
    return render(request, 'main/our_team.html')



