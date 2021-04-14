from membership.models import Subscription
from datetime import datetime, timedelta


def cleanup_expired_subscriptions():
    # Deleted expired subscriptions
    Subscription.objects.filter(
            expire_date_subscription__lte=datetime.now() -
            timedelta(
                days=1)).delete()
