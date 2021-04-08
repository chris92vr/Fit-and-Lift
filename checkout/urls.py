from django.urls import path
from . import views


urlpatterns = [
    path('membership/<int:membership_id>/', views.checkout_membership,
         name='checkout_membership'),
    path('membership/payment/<int:membership_id>',
         views.membership_success,
         name='membership_success'),
    path('subscription/<int:subscription_id>/',
         views.update_subscription_checkout,
         name='update_subscription_checkout'),
    path('subscription_success/<int:subscription_id>/',
         views.update_subscription_checkout_success,
         name='update_subscription_checkout_success'),
    path('webhook/', views.stripe_webhook),
]
