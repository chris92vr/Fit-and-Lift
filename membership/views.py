from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from datetime import timedelta

from membership.models import Membership, Subscription


# Create your views here.


def membership(request):
    """ renders all membership"""

    membership = Membership.objects.all()
    context = {
        'membership': membership,

    }

    return render(request, 'membership/membership.html', context)


@login_required
def membership_detail(request, membership_id):
    """ Renders the product details """

    membership = get_object_or_404(Membership, pk=membership_id)
    subscription = Subscription.objects.all()

    date = None
    exp_date = 0
    if request.method == 'POST':
        date_str = request.POST.get('date')
        date = parse_date(date_str)
        exp_date = date + timedelta(days=membership.duration_days)

    exp_date = exp_date

    context = {
        'membership': membership,
        'subscription': subscription,
        'date': date,
        'exp_date': exp_date,
    }

    return render(request, 'membership/membership_detail.html', context)
