from django.db import models
from helpers.models import BaseModel
# from django.contrib.auth import get_user_model
from django.conf import settings
from ..models.location import Location

# User = get_user_model()
User = settings.AUTH_USER_MODEL


class Branch(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='my_branch', db_index=True)
    branch_name = models.CharField(max_length=150, db_index=True)
    phone_number = models.CharField(max_length=15, db_index=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, db_index=True)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.branch_name
