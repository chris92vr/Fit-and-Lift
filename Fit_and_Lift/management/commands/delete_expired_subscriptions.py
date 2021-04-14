from django.core.management.base import NoArgsCommand
from membership.models import Subscription
import datetime as dt

class Command(NoArgsCommand):

    help = 'Expires event objects which are out-of-date'

    def handle_noargs(self):
        Subscription.objects.filter(date__lt=dt.date.today()).delete()