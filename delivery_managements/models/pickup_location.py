from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings
from helpers.models import BaseModel
from ..models.branch import Branch

# User = get_user_model()
User = settings.AUTH_USER_MODEL


class PickupLocation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pickup_location', db_index=True)
    pickup_name = models.CharField(_('picup name'), max_length=150)
    pickup_address = models.CharField(_('picup address'), max_length=250)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    pickup_phone_number = models.CharField(_('pickup phone number'), max_length=50, db_index=True)

    def __str__(self) -> str:
        return f"{self.pickup_name} -> {self.pickup_phone_number}"

    class Meta:
        verbose_name = "pickup location"
        verbose_name_plural = "pickup locations"

