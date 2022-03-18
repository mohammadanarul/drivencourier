from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import PickupLocation
from .forms import PicupLocationForm


class PickupLocationListView(ListView):
    model = PickupLocation
    template_name = "pickuplocation/pickup-location-list.html"

    def get_queryset(self):
        qs = super(PickupLocationListView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class PickupLocationCreateView(CreateView):
    template_name = "pickuplocation/create-and-update-picuplocation.html"
    form_class = PicupLocationForm
    success_url = reverse_lazy('pickuplocations:pickup_location_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PickupLocationCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create Pickup Location'
        return context

class PickupLocationUpdateView(UpdateView):
    model = PickupLocation
    template_name = "pickuplocation/create-and-update-picuplocation.html"
    form_class = PicupLocationForm
    success_url = reverse_lazy('pickuplocations:pickup_location_list')

    # def form_valid(self, form):
    #     return super(PickupLocationUpdateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Update Pickup Location'
        return context

