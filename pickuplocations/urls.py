from django.urls import path
from .views import (
    PickupLocationListView,
    PickupLocationCreateView,
    PickupLocationUpdateView,
)

app_name = 'pickuplocations'
urlpatterns = [
    path('pickup-location-list/', PickupLocationListView.as_view(), name='pickup_location_list'),
    path('pickup-location-create/', PickupLocationCreateView.as_view(), name='pickup_location_create_view'),
    path('pickup-location-update/<int:pk>/', PickupLocationUpdateView.as_view(), name='pickup_location_update_view'),
]