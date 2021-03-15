from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import timedelta
from django.contrib.auth.models import User
import datetime as dt
from django.contrib.auth.decorators import login_required
import datetime
from membership.models import Membership, UserMembership, Subscription
from profiles.models import UserProfile
import stripe

@login_required
def checkout_membership(request, membership_id):
    """ 
    Renders membership checkout page 
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    membership = get_object_or_404(Membership, pk=membership_id)
    profile = UserProfile.objects.get(user=request.user)
    date = dt.date.today()
    exp_date = 0
    if request.GET:
        exp_date = date + timedelta(days=membership.duration_days)
        mem_type = request.session.get('mem_type', {})
        mem_type = membership.membership_type
        request.session['mem_type'] = mem_type
        member = request.session.get('member', {})
        member = date.strftime('%m/%d/%Y')
        member_exp_date = request.session.get('member_exp_date', {})
        member_exp_date = exp_date.strftime('%m/%d/%Y')
        request.session['member'] = member
        request.session['member_exp_date'] = member_exp_date
    if request.method == 'POST':
        pid = request.POST.get('client_secret').split('_secret')[0]
        membership.stripe_pid = pid
        return redirect(reverse('membership_success', args=[membership_id]))

    stripe_total = round(membership.price * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = stripe_total, currency=settings.STRIPE_CURRENCY,)

    template = 'checkout/checkout_membership.html'
    context = {
        'membership': membership,
        'date': date,
        'profile': profile,
        'exp_date': exp_date,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context,)


@login_required
def membership_success(request, membership_id):
    """
    renders the view for membership success checkput
    """
    membership = get_object_or_404(Membership, pk=membership_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    profile1 = get_object_or_404(User, username=request.user)
    usermembership = UserMembership.objects.create(member_profile = profile, user_membership = membership)
    profile_name = profile.user
    duration_days = membership.duration_days
    s = Subscription.objects.create(subcription_membership = usermembership,  membership_duration = membership)
    
    date = dt.date.today()
    exp_date = date + timedelta(days=membership.duration_days)

    profile.is_subscribed = True
    profile.expire_date_subscription = exp_date
    profile.save()
    # Sends confirmation email to the customer
    cust_email = profile1.email
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt')
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )    
    messages.success(request, f'Order successfully processed! \
        Your membership active is {membership.membership_type}.')
    template = 'checkout/checkout_membership_success.html'
    context = {
        'exp_date': exp_date,
        'membership': membership,
        'profile_name': profile_name,
        'duration_days': duration_days,
    }
    return render(request, template, context)
