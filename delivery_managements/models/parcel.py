from django.db import models
from helpers.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from ..models.pickup_location import PickupLocation
from ..models.branch import Branch

User = settings.AUTH_USER_MODEL


class Parcel(BaseModel):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancel', 'Cancel'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parcels')
    tracking_id = models.CharField(_('tracking id'), blank=True, max_length=12, unique=True, db_index=True)
    customer_name = models.CharField(_('customer name'), max_length=100)
    customer_phone_number = models.CharField(_('customer phone number'), max_length=100, db_index=True)
    customer_address = models.CharField(_('customer address'), max_length=250)
    pickup_location = models.ForeignKey(PickupLocation, on_delete=models.SET_NULL, null=True, blank=True)
    parcel_weight = models.CharField(_('parcel weight'), max_length=10, default='500gm')
    delivery_location = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True,
                                          verbose_name='delivery location', db_index=True)
    product_selling_price = models.CharField(_('product selling price'), max_length=15)
    product_category = models.CharField(_('product category'), max_length=100)
    description = models.TextField(_('description'), max_length=350)
    status = models.CharField(_('status'), choices=STATUS_CHOICES, default='Pending', max_length=15, db_index=True)

    def __str__(self):
        return f"{self.user}->{self.delivery_location}"
