from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Membership


# Create your views here.


def all_membership(request):
    """ renders all membership"""

    memberships = Membership.objects.all()
    context = {
        'memberships': memberships,

    }

    return render(request, 'membership/membership.html', context)


def membership_detail(request, membership_id):
    """ A view to show individual membership details """

    membership = get_object_or_404(Membership, pk=membership_id)

    context = {
        'membership': membership,
    }

    return render(request, 'membership/membership_detail.html', context)