from pickle import TRUE
from statistics import mode
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from helpers.models import BaseModel
from locations.models import Location

class PickupLocation(BaseModel):
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pickup_location')
    pickup_name = models.CharField(_('picup name'), max_length=150)
    pickup_address = models.CharField(_('picup address'), max_length=250)
    pickup_area = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=('pickup area'))
    pickup_phone_number  = models.CharField(_('pickup phone number'), max_length=50)

    def __str__(self) -> str:
        return f"{self.pickup_name} -> {self.pickup_phone_number}"
    
    class Meta:
        ordering = ['-pk']
