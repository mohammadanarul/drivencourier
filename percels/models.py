from re import T
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from helpers.models import BaseModel
from helpers.utils import UNIQUE_TRAKING_NUMBER
from locations.models import Location
from accounts.models import Rider
from pickuplocations.models import PickupLocation

class Percel(BaseModel):
    STATUS_CHOICES = (
        ('Approved', 'Approved'),
        ('PickupPending', 'PickupPending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancel', 'Cancel'),
        ('Return', 'Return'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='percel', verbose_name='percel')
    traking_id = models.CharField(_('traking id'), max_length=12)
    customer_name = models.CharField(('customer name'), max_length=100)
    customer_phone_number = models.CharField(_('customer phone number'), max_length=100)
    customer_address = models.CharField(_('customer address'), max_length=250)
    pickup_location = models.ForeignKey(PickupLocation, on_delete=models.SET_NULL, null=True, blank=True)
    parcel_weight = models.CharField(_('percel weight'), max_length=10, default='500gm')
    delivery_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='delivery location')
    product_selling_price = models.CharField(_('product selling price'), max_length=15)
    product_category = models.CharField(_('product category'), max_length=100)
    description = models.TextField(_('description'), max_length=350)
    delivery_by = models.ForeignKey(Rider, on_delete=models.SET_NULL, null=True, blank=True, related_name='percel_delivery',
     verbose_name='delivery by')
    pickup_by = models.ForeignKey(Rider, on_delete=models.SET_NULL, null=True, blank=True, related_name='percel_pickup', verbose_name='pickup by')
    status = models.CharField(_('status'), choices=STATUS_CHOICES, default='PickupPending', max_length=15)

    def __str__(self):
        return f"{self.user}->{self.delivery_location}"
    
    def save(self, *args, **kwargs):
        if not self.traking_id:
            self.traking_id = UNIQUE_TRAKING_NUMBER
        super(Percel, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-pk']
    

