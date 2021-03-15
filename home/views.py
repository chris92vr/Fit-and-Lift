from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject= form.cleaned_data.get("subject")
        contact_email = form.cleaned_data.get("contact_email")
        content = form.cleaned_data.get("content")
        content = " with the email, " + contact_email + ", sent the following message:\n\n" + content;
        send_mail(subject, content, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
        context = {'form': form}
        return render(request, 'home/contact_us.html', context)
    else:
        context = {'form': form}
        return render(request, 'home/contact_us.html', context)



