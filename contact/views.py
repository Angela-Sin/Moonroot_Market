from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # You can save the message to DB or send an email
        subject = f"Contact Form: {form.cleaned_data['name']}"
        message = form.cleaned_data['message']
        sender = form.cleaned_data['email']
        recipients = [settings.DEFAULT_FROM_EMAIL]

        send_mail(subject, message, sender, recipients)
        return redirect('contact:success')
    return render(request, 'contact/contact_form.html', {'form': form})


def success_view(request):
    return render(request, 'contact/success.html')
