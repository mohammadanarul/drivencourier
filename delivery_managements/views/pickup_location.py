from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.pickup_location import PickupLocation
from ..forms.pickup_location import PicupLocationForm


class PickupLocationListView(LoginRequiredMixin, ListView):
    model = PickupLocation
    template_name = "pickup_location/list.html"
    success_url = '/pickup-location/'

    def get_queryset(self):
        qs = super(PickupLocationListView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create Pickup Location'
        return context


class PickupLocationCreateView(LoginRequiredMixin, CreateView):
    model = PickupLocation
    template_name = "common_form/create-and-update.html"
    form_class = PicupLocationForm
    success_url = '/pickup-location/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PickupLocationCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create a Pickup Location'
        return context


class PickupLocationUpdateView(LoginRequiredMixin, UpdateView):
    model = PickupLocation
    template_name = "common_form/create-and-update.html"
    form_class = PicupLocationForm
    success_url = '/pickup-location/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PickupLocationUpdateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Update Pickup Location'
        return context


class PickupLocationDeleteView(LoginRequiredMixin, DeleteView):
    model = PickupLocation
    success_url = '/pickup-location/'
