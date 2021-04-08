from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from membership.models import UserMembership, Subscription
import datetime as dt


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    try:
        profile = UserProfile.objects.get(user=request.user)
        usermembership = get_object_or_404(
            UserMembership, member_profile=profile)
        subscription = get_object_or_404(
            Subscription, subcription_membership=usermembership)
    except BaseException:
        usermembership = None
        subscription = None
        profile = None
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'subscription': subscription,

    }

    return render(request, template, context)
