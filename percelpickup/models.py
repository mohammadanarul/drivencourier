from django.db import models
from percels.models import Percel
from helpers.models import BaseModel
from accounts.models import Rider, Manager
from django.contrib.auth import get_user_model

User = get_user_model()

class PercelPickup(BaseModel):
    PICKUP_STATUS = (
        ('Pending', 'Pending'),
        ('Accept', 'Accept'),
        ('Completed', 'Completed'),
        ('Cance', 'Cance')
    )
    pickuped_to = models.ForeignKey(Manager,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='pickuped_to')
    pickup_by = models.ForeignKey(Rider,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='pickup_by')
    percel = models.ForeignKey(Percel, on_delete=models.PROTECT, related_name='percel_pickup')
    status = models.CharField(choices=PICKUP_STATUS, default='Pending', max_length=10)

    @property
    def location(self):
        return self.percel.pickup_location.pickup_area

