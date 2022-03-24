from django.db import models
from percels.models import Percel
from helpers.models import BaseModel
from accounts.models import Rider, Manager
from django.contrib.auth import get_user_model

User = get_user_model()

class PercelPickup(BaseModel):
    pickuped_to = models.ForeignKey(Manager, on_delete=models.PROTECT, related_name='pickuped_to')
    pickup_by = models.ForeignKey(Rider, on_delete=models.PROTECT, related_name='pickup_by')
    percel = models.ForeignKey(Percel, on_delete=models.PROTECT, related_name='percel_pickup')
    completed = models.BooleanField(default=False)

