from django.apps import AppConfig


class SubscriptionConfig(AppConfig):
    name = 'Fit_and_Lift'

    def ready(self):
        from . import updater
        updater.start()