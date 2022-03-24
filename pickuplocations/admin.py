from django.contrib import admin
from .models import PickupLocation


@admin.register(PickupLocation)
class PickupLocationAdmin(admin.ModelAdmin):
    list_display  = ['pickup_name',]