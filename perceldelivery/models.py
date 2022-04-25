from email.mime.image import MIMEImage
from django.db import models
from percels.models import Percel
from helpers.models import BaseModel
from accounts.models import Rider, Manager


class PercelDelivery(BaseModel):
    DELIVERY_STATUS = (
        ('Pending', 'Pending'),
        ('Accept', 'Accept'),
        ('Completed', 'Completed'),
        ('Cance', 'Cance')
    )
    delivery_to = models.ForeignKey(Manager,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='delivery_to')
    delivery_by = models.ForeignKey(Rider,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='delivery_by', verbose_name='delivery by')
    percel = models.ForeignKey(Percel, on_delete=models.PROTECT, related_name='percel_delivey')
    status = models.CharField(choices=DELIVERY_STATUS, default='Pending', max_length=10)


