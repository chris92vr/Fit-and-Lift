from membership.models import Subscription
import datetime as dt

def cleanup_expired_subscriptions():
    # Deleted expired subscriptions
    date = dt.date.today()
    Subscription.objects.filter(
            expire_date_subscription__lt=date).delete()
