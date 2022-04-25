from django.urls import path
from .views import (
    PercelPickupCreateView,
    percel_pickup_accept,
    percel_pickup_completed,
)

app_name = 'percelpickup'
urlpatterns = [
    path('pickup-created/', PercelPickupCreateView.as_view(), name='percel_pickup_created'),
    path('pickup-accept/<int:pk>/', percel_pickup_accept, name='percel_pickup_accept'),
    path('pickup-accept-complte/<int:pk>/', percel_pickup_completed, name='percel_pickup_accepted_manager')
    # path('pickup-accept/<int:pk>/', PercelPickupAcceptedView.as_view(), name='percel_pickup_accept'),
]