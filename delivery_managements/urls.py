from django.urls import path
from .views import (
    parcel,
    pickup_location,
    location,
    branch,
    parcel_pickup,
    parcel_delivery,
    shipment,
)

urlpatterns = [
    # parcel view url
    path('', parcel.HomeView.as_view(), name='home_view'),
    path('dashboard/', parcel.DashboardView.as_view(), name='dashboard_view'),
    path('parcels/', parcel.ParcelListView.as_view(), name='parcel_list_view'),
    path('parcel-create/', parcel.ParcelCreateView.as_view(), name='parcel_create_view'),
    path('parcel-update/<pk>/', parcel.ParcelUpdateView.as_view(), name='parcel_update_view'),
    # locations urls
    path('locations/', location.LocationCreateAndListView.as_view(), name='location_list_view'),
    path('location-create/', location.LocationCreateView.as_view(), name='location_create_view'),
    path('location-update/<pk>/', location.LocationUpdateView.as_view(), name='location_update_view'),
    path('location-delete/<pk>/', location.LocationDeleteView.as_view(), name='location_delete_view'),
    # branch urls
    path('branch/', branch.BranchCreateAndListView.as_view(), name='branch_list_view'),
    path('branch-create/', branch.BranchCreateView.as_view(), name='branch_create_view'),
    path('branch-update/<pk>/', branch.BranchUpdateView.as_view(), name='branch_update_view'),
    path('branch-delete/<pk>', branch.BranchDeleteView.as_view(), name='branch_delete_view'),
    # pickup location urls
    path('pickup-location/', pickup_location.PickupLocationListView.as_view(),
         name='pickup_location_list_view'),
    path('pickup-create/', pickup_location.PickupLocationCreateView.as_view(),
         name='pickup_location_create_view'),
    path('pickup-location-update/<pk>/', pickup_location.PickupLocationUpdateView.as_view(),
         name='pickup_location_update_view'),
    path('pickup-location-delete/<pk>/', pickup_location.PickupLocationDeleteView.as_view(),
         name='pickup_location_delete_view'),
    # parcel pickup urls
    path('parcel-pickup/', parcel_pickup.ParcelPickupListView.as_view(),
         name='parcel_pickup_list_view'),
    path('parcel-pickup-create/', parcel_pickup.ParcelPickupCreateView.as_view(),
         name='parcel_pickup_create_view'),
    path('parcel-pickup-update/<pk>/', parcel_pickup.ParcelPickupUpdateView.as_view(),
         name='parcel_pickup_update_view'),
    path('parcel-pickup-delete/<pk>/', parcel_pickup.ParcelPickupDeleteView.as_view(),
         name='parcel_pickup_delete_view'),
    # parcel delivery urls
    path('parcel-delivery-list/', parcel_delivery.ParcelDeliveryListView.as_view(),
         name='parcel_delivery_list_view'),
    path('parcel-delivery-create/', parcel_delivery.ParcelDeliveryCreateView.as_view(),
         name='parcel_delivery_create_view'),
    path('parcel-delivery-update/<pk>/', parcel_delivery.ParcelDeliveryUpdateView.as_view(),
         name='parcel_delivery_update_view'),
    path('parcel-delivery-delete/<pk>/', parcel_delivery.ParcelDeliveryUpdateView.as_view(),
         name='parcel_delivery_delete_view'),
    # Shipment delivery urls
    path('shipment-list', shipment.ShipmentListView.as_view(),
         name='shipment_list_view'),
    path('shipment-create/', shipment.ShipmentCreateView.as_view(),
         name='shipment_create_view'),
    path('shipment-update/<pk>/', shipment.ShipmentUpdateView.as_view(),
         name='shipment_update_view'),
    path('shipment-delete/<pk>/', shipment.ShipmentDeleteView.as_view(),
         name='shipment_delete_view'),

]


