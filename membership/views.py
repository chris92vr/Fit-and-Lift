from django.shortcuts import render, get_object_or_404
from membership.models import Membership, Subscription
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required
import datetime as dt


def membership(request):
    """ renders all membership"""
    membership = Membership.objects.all()
    date = dt.date.today()
    try:
        profile = UserProfile.objects.get(user=request.user)
        subscription = get_object_or_404(Subscription,
                                         member_profile=profile
                                         )
    except:
        subscription = None
        profile = None
    context = {
        'membership': membership,
        'subscription': subscription,
        'date': date,
    }
    return render(request, 'membership/membership.html', context)


@login_required
def edit_subscription(request, subscription_id):
    """ Extends subscription """
    extended_days = 0
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    if request.method == 'GET':
        extended_days = request.GET.get('extended_subscription_days')
        request.session['extended'] = extended_days
    template = 'membership/edit_subscription.html'
    context = {
        'subscription': subscription,
    }
    return render(request, template, context)
