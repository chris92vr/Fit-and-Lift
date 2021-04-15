from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from membership.models import UserMembership, Subscription, Membership
from django.contrib.auth.models import User
import datetime as dt
from django.contrib import messages
import datetime as dt


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    # Delete expired subscriptions
    date = dt.date.today()
    subscriptions_expired = Subscription.objects.filter(
        expire_date_subscription__lt=date)
    for subscription in subscriptions_expired:
        usermembership = get_object_or_404(
            UserMembership, subscription_number=subscription.user_membership)
        usermembership.delete()
    membership = Membership.objects.all()
    try:
        profile = UserProfile.objects.get(user=request.user)
        usermembership = get_object_or_404(
            UserMembership, member_profile=profile)
        subscription = get_object_or_404(
            Subscription, user_membership=usermembership)
        membership = get_object_or_404(
            Membership, name=usermembership.user_membership)
    except BaseException:
        usermembership = None
        subscription = None
        profile = None
        membership = None
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'subscription': subscription,
        'membership': membership,
    }

    return render(request, template, context)


@login_required
def delete_accont(request):
    """ Remove profile from db """
    profile = get_object_or_404(User, username=request.user)
    profile.delete()
    messages.success(request, 'account deleted!')
    return render(request, 'home/index.html')
