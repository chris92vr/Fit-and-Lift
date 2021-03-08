from django.db import models

from profiles.models import UserProfile
from datetime import datetime, timedelta



# Create your models here.


class Membership(models.Model):
    """
    Model for membership
    """
    frequency = [
        ('weekly', ('Weekly')),
        ('monthly', ('Monthly')),
        ('annually', ('Annually')),
    ]
    
    name = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    duration_days = models.IntegerField(default="30")
    membership_type = models.CharField(
        choices=frequency, default='monthly',
        max_length=30, null=True
    )
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.membership_type
    


class UserMembership(models.Model):
    """
    Model for user profile membeship
    """
    member_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                       null=True, blank=False,
                                       related_name='member')
    user_membership = models.ForeignKey(
        Membership, related_name='user_membership', on_delete=models.SET_NULL, null=True)
    @classmethod
    def create(cls, member_profile, user_membership):
        usermembership = cls(member_profile=member_profile, user_membership=user_membership)
        # do something with the book
        return usermembership


class Subscription(models.Model):
    """
    Model for Subsciption
    """
    subcription_membership = models.ForeignKey(
        UserMembership, related_name='subscription', on_delete=models.CASCADE, null=True)
    membership_duration = models.ForeignKey(
        Membership, related_name='duration', on_delete=models.CASCADE, default="")
    purchase_date = models.DateField(default=datetime.today)
    @property
    def expected_return(self, IntegerField):
       
        return self.purchase_date + datetime.timedelta(days=IntegerField)

   
     


    