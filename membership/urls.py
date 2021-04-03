from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership, name='membership'),
    path('edit/<int:subscription_id>/',
         views.edit_subscription, name='edit_subscription'),
]
