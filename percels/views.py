from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView
)
from django.urls import reverse_lazy
from django.contrib import messages
from pickuplocations.models import PickupLocation
from .models import Percel
from .forms import PercelForm


class HomeView(TemplateView):
    template_name = "home.html"

class PercelListView(ListView):
    model = Percel
    template_name = "percels/percel-list.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(PercelListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs


class PercelCreateView(CreateView):
    template_name = 'percels/create_and_update_percel.html'
    form_class = PercelForm
    success_url = reverse_lazy('percels:percels_view')

    def form_valid(self, form):
        messages.success(self.request, 'Created percel')
        return super(PercelCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        kwargs['pickup_location'] = self.request.user.pickup_location.all()
        context =  super(PercelCreateView, self).get_context_data(**kwargs)
        context["title"] = 'Create Percel'
        return context

class PercelUpdateView(UpdateView):
    model = Percel
    template_name = 'percels/create_and_update_percel.html'
    form_class = PercelForm
    success_url = reverse_lazy('percels:percels_view')

    def form_valid(self, form):
        messages.success(self.request, 'updated percel')
        return super(PercelUpdateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        kwargs['pickup_location'] = self.request.user.pickup_location.all()
        context =  super(PercelUpdateView, self).get_context_data(**kwargs)
        context["title"] = 'Update Percel'
        return context

