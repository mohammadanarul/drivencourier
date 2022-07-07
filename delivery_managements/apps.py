from django.apps import AppConfig


class DeliveryManagementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'delivery_managements'

    def ready(self):
        import delivery_managements.signals
