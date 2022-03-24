from django.urls import path
from .views import PercelPickupCreateView

app_name = 'percelpickup'
urlpatterns = [
    path('pickup-created/', PercelPickupCreateView.as_view(), name='percel_pickup_created'),
]