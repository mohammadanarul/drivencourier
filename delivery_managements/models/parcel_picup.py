from django.db import models
from accounts.models import Rider
from helpers.models import BaseModel
from django.contrib.auth import get_user_model
from django.conf import settings
from ..models.parcel import Parcel

# User = get_user_model()
User = settings.AUTH_USER_MODEL


class ParcelPickup(BaseModel):
    STATUS_CHOICES = (
        ('Accept', 'Accept'),
        ('Pending', 'Pending'),
        ('PC', 'Pickup Complete'),
    )
    pickup_to = models.ForeignKey(User, on_delete=models.PROTECT, related_name='pickup_to', db_index=True)
    pickup_by = models.ForeignKey(Rider, on_delete=models.PROTECT, blank=True, related_name='pickup_by', db_index=True)
    parcel = models.ManyToManyField(Parcel, related_name='parcel_pickup')
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='Pending', db_index=True)

    class Meta:
        verbose_name = "Parcel Pickup"
        verbose_name_plural = "Parcel Pickup"
