from django.db import models
from accounts.models import Rider
from helpers.models import BaseModel
from django.contrib.auth import get_user_model
from django.conf import settings
from ..models.parcel import Parcel

# User = get_user_model()
User = settings.AUTH_USER_MODEL


class ParcelDelivery(BaseModel):
    STATUS_CHOICES = (
        ('Accept', 'Accept'),
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    )
    delivery_to = models.ForeignKey(User, on_delete=models.PROTECT, related_name='delivery_to', db_index=True)
    delivery_rider = models.ForeignKey(Rider, on_delete=models.PROTECT, blank=True, related_name='delivery_rider')
    parcel = models.ManyToManyField(Parcel, related_name='parcel_delivery')
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='Pending', db_index=True)

    class Meta:
        verbose_name = "Parcel Delivery"
        verbose_name_plural = "Parcel Deliveries"
