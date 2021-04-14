from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from profiles.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from membership.models import UserMembership, Subscription
import datetime as dt
from profiles.models import UserProfile


def index(request):
    """ A view to return the index page """
    date = dt.date.today()
    profile = UserProfile.objects.get(user=request.user)
    subscriptions_expired=Subscription.objects.filter(
            expire_date_subscription__lt=date)
    for subscription in subscriptions_expired:
        usermembership = get_object_or_404(
        UserMembership, member_profile=profile)
        usermembership.delete()
    subscriptions_expired.delete()
    
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
