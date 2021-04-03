from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from profiles.models import UserProfile


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def contact(request):
    """ Renders a contact form """
    form = ContactForm(request.POST or None)
    profile = get_object_or_404(UserProfile, user=request.user)
    if form.is_valid():
        subject = form.cleaned_data.get("subject")
        contact_email = form.cleaned_data.get("contact_email")
        content = form.cleaned_data.get("content")
        content = " with the email, " + contact_email + \
            ", sent the following message:\n\n" + content
        send_mail(
            subject, content, settings.DEFAULT_FROM_EMAIL, [
                settings.DEFAULT_FROM_EMAIL])
        context = {'profile': profile}
        return render(request, 'home/contact_us_success.html', context)
    else:
        context = {'form': form}
        return render(request, 'home/contact_us.html', context)
