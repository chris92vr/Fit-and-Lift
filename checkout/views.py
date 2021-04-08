from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import timedelta
from django.contrib.auth.models import User
import datetime as dt
from django.contrib.auth.decorators import login_required
import datetime
import datetime as dt
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

    date = dt.date.today()

    membership = get_object_or_404(Membership, pk=membership_id)

    try:
        profile = UserProfile.objects.get(user=request.user)
        usermembership = get_object_or_404(UserMembership,
                                           member_profile=profile)
        subscription = get_object_or_404(Subscription,
                                         subcription_membership=usermembership
                                         )
    except:
        usermembership = None
        subscription = None
        profile = None
    
    if request.method == 'POST':
        pid = request.POST.get('client_secret').split('_secret')[0]
        membership.stripe_pid = pid
        return redirect(reverse('membership_success', args=[membership_id]))

    stripe_total = round(membership.price * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total, currency=settings.STRIPE_CURRENCY,)

    template = 'checkout/checkout_membership.html'
    context = {
        'membership': membership,
        'subscription': subscription,
        'date': date,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context,)


@login_required
def membership_success(request, membership_id):
    """
    renders the view for membership success checkout
    """
    membership = get_object_or_404(Membership, pk=membership_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    profile1 = get_object_or_404(User, username=request.user)
    usermembership = UserMembership.objects.create(member_profile=profile,
                                                   user_membership=membership)
    profile_name = profile.user
    duration_days = membership.duration_days
    date = dt.date.today()
    exp_date = date + timedelta(days=membership.duration_days)
    Subscription.objects.create(subcription_membership=usermembership,
                                membership_duration=membership,
                                is_subscribed=True,
                                expire_date_subscription=exp_date,
                                duration_days=duration_days)
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

    messages.success(request, f'Subscription successfully processed! \
        Your membership active is {membership.membership_type}, \
        valid till { exp_date }. ')
    template = 'checkout/checkout_membership_success.html'
    context = {
        'exp_date': exp_date,
        'membership': membership,
        'profile_name': profile_name,
        'duration_days': duration_days,
    }
    return render(request, template, context)


@login_required
def update_subscription_checkout(request, subscription_id):
    """
    Renders extend membership checkout page
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    subscription = get_object_or_404(Subscription, pk=subscription_id)
    price = None
    extended_days = None

    if request.method == 'GET':
        extended_days = request.GET.get('extended_subscription_days')
        extended_days = int(extended_days)
        extended = request.session.get('extended', {})
        extended = extended_days
        request.session['extended'] = extended
        date = subscription.expire_date_subscription
        expire_date = date + timedelta(days=extended_days)

    if request.method == 'POST':
        pid = request.POST.get('client_secret').split('_secret')[0]
        subscription.stripe_pid = pid
        return redirect(reverse('update_subscription_checkout_success',
                                args=[subscription_id]))

    if extended_days == 7:
        price = 15
    elif extended_days == 30:
        price = 50
    elif extended_days == 365:
        price = 500
    stripe_total = round(price * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total, currency=settings.STRIPE_CURRENCY,)

    template = 'checkout/update_subscription_checkout.html'
    context = {
        'subscription': subscription,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'stripe_total': stripe_total,
        'expire_date': expire_date,
        'price': price,
        }
    return render(request, template, context,)


@login_required
def update_subscription_checkout_success(request, subscription_id):
    """
    Renders extend membership checkout page
    """
    subscription = get_object_or_404(Subscription, pk=subscription_id)
    extended_subscription_days = request.session.get('extended')
    subscription.extended_subscription_days = int(extended_subscription_days)
    date = subscription.expire_date_subscription
    exp_date = date + timedelta(days=subscription.extended_subscription_days)
    subscription.expire_date_subscription = exp_date
    subscription.duration_days = subscription.duration_days
    + subscription.extended_subscription_days
    subscription.save()
    profile = get_object_or_404(UserProfile, user=request.user)
    profile_name = profile.user
    profile1 = get_object_or_404(User, username=request.user)

    # Sends confirmation email to the customer
    cust_email = profile1.email
    subject = render_to_string(
        '''checkout/confirmation_emails/
        confirmation_email_subscription_subject.txt''')
    body = render_to_string(
        '''checkout/confirmation_emails/
        confirmation_email_subscription_subject.txt''',
        {'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )

    messages.success(request, f'Subscription successfully extended! \
        Your membership is  valid till {exp_date}.')
    template = 'checkout/update_subscription_checkout_success.html'
    context = {
        'exp_date': exp_date,
        'subscription': subscription,
        'profile_name': profile_name,
        }
    return render(request, template, context)

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_WH_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)