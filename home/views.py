from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from profiles.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


@login_required
def contact(request):
    """ Renders a contact form """
    form = ContactForm(request.POST or None)
    profileUser = get_object_or_404(User, username=request.user)
    if form.is_valid():
        subject = form.cleaned_data.get("subject")
        contact_email = profileUser.email
        content = form.cleaned_data.get("content")
        content = " with the email, " + contact_email + \
            ", sent the following message:\n\n" + content
        send_mail(
            subject, content, settings.DEFAULT_FROM_EMAIL, [
                settings.DEFAULT_FROM_EMAIL])
        context = {'profile': profileUser}
        return render(request, 'home/contact_us_success.html', context)
    else:
        context = {'form': form}
        return render(request, 'home/contact_us.html', context)
