from django.urls import path
from .views import (
    HomeView,
    PercelListView,
    PercelCreateView,
    PercelUpdateView,
)

app_name = 'percels'
urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('percels/', PercelListView.as_view(), name='percels_view'),
    path('percels-create/', PercelCreateView.as_view(), name='percels_create_view'),
    path('percels-update/<int:pk>/', PercelUpdateView.as_view(), name='percels_update_view'),
]