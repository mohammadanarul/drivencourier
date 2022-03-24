from email.mime.image import MIMEImage
from django.db import models
from percels.models import Percel
from helpers.models import BaseModel
from accounts.models import Rider, Manager


class PercelDelivery(BaseModel):
    delivery_to = models.ForeignKey(Manager, on_delete=models.PROTECT, related_name='delivery_to')
    delivery_by = models.ForeignKey(Rider, on_delete=models.PROTECT,
        related_name='delivery_by', verbose_name='delivery by')
    percel = models.ForeignKey(Percel, on_delete=models.PROTECT, related_name='percel_delivey')
    bar_code = models.ImageField(upload_to='delivery-barcode/')
    completed = models.BooleanField(default=False)


