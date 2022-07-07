from django.contrib import admin
from .models.parcel import Parcel
from .models.location import Location
from .models.branch import Branch
from .models.pickup_location import PickupLocation
from .models.parcel_picup import ParcelPickup
from .models.parcel_delivery import ParcelDelivery
from .models.shipment import Shipment


admin.site.register([Parcel, Location, Branch, PickupLocation, Shipment, ParcelPickup, ParcelDelivery])
