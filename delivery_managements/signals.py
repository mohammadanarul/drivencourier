import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.parcel import Parcel


@receiver(post_save, sender=Parcel)
def save_parcel_tracking_id(sender, instance, **kwargs):
    if not instance.tracking_id:
        instance.tracking_id = str(uuid.uuid4()).replace('-', '').upper()[:12]
        instance.save()
