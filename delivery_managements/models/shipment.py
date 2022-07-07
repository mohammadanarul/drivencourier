from django.db import models
from helpers.models import BaseModel
from django.contrib.auth import get_user_model
from django.conf import settings
from .branch import Branch
from ..models.parcel import Parcel

# User = get_user_model()
User = settings.AUTH_USER_MODEL


class Shipment(BaseModel):
    STATUS_CHOICES = (
        ('Accept', 'Accept'),
        ('Pending', 'Pending'),
        ('SC', 'Shipment Completed'),
        ('Return', 'Return'),
    )

    shipment_to = models.ForeignKey(User, on_delete=models.PROTECT, related_name='shipments')
    parcel = models.ManyToManyField(Parcel)
    sender_branch = models.ForeignKey(Branch, on_delete=models.PROTECT,
                                      related_name='shipment_sender_branch', db_index=True)
    receiver_branch = models.ForeignKey(Branch, on_delete=models.PROTECT,
                                        related_name='shipment_receiver_branch', db_index=True)
    truck_diver_name = models.CharField(max_length=50)
    truck_diver_phone_number = models.CharField(max_length=15, db_index=True)
    truck_plate_number = models.CharField(max_length=50, db_index=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending', db_index=True)
