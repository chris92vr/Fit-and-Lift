from django.core.management.base import BaseCommand, CommandError
from membership.models import Subscription
import datetime as dt


class Command(BaseCommand):
    help = 'Delete expired subscriptions in the database'

    def handle(self):
      
        subscriptions = Subscription.objects.all()
        for subscription in subscriptions:
            if subscription.expire_date_subscription < dt.date.today():
                subscription.delete()
        return
