from django.db import models
from profiles.models import UserProfile
from datetime import datetime


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
    duration_days = models.IntegerField(default="30")
    membership_type = models.CharField(
        choices=frequency, default='monthly',
        max_length=30, null=True
    )
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class UserMembership(models.Model):
    """
    Model for user profile membeship
    """
    member_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                       null=True, blank=False,
                                       related_name='member')
    user_membership = models.ForeignKey(
        Membership,
        related_name='user_membership',
        on_delete=models.CASCADE,
        null=True)


class Subscription(models.Model):
    """
    Model for Subsciption
    """

    subscription_membership = models.ForeignKey(
        UserMembership,
        related_name='subscription',
        on_delete=models.CASCADE,
        null=True)
    expire_date_subscription = models.DateField(null=True)
    purchase_date = models.DateField(default=datetime.today)
    duration_days = models.IntegerField(default=30)
    extended_subscription_days = models.IntegerField(null=True)

    @property
    def registration_deadline(self, IntegerField):

        return self.purchase_date + datetime.timedelta(days=IntegerField)
