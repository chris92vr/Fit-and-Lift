from django.urls import path
from . import views


urlpatterns = [
    path('membership/<int:membership_id>/', views.checkout_membership,
         name='checkout_membership'),
    path('membership/payment/<int:membership_id>',
         views.membership_success,
         name='membership_success'),

]