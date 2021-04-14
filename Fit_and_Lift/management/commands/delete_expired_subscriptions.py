from django.core.management.base import BaseCommand
from Fit_and_Lift.deleted_expired_subscriptions import cleanup_expired_subscriptions

class Command(BaseCommand):
    def handle(self, *args, **options):

        # Delete expired subscriptions
        cleanup_expired_subscriptions()






