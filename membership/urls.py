from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_membership, name='membership'),
    path('<int:membership_id>/', views.membership_detail,
         name='membership_detail'),
]