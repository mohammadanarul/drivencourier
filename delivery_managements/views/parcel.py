from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView
)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.parcel import Parcel
from ..models.parcel_picup import ParcelPickup
from ..forms.parcel import ParcelForm


class HomeView(TemplateView):
    template_name = "landing.html"


class DashboardView(LoginRequiredMixin, ListView):
    model = Parcel
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(DashboardView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context["pickup_parcel_list"] = ParcelPickup.objects.filter(status='Pending')
        context["parcel_pickup_manager_accepted"] = ParcelPickup.objects.filter(status='Accept')
        return context


class ParcelListView(LoginRequiredMixin, ListView):
    model = Parcel
    template_name = "parcel/list.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(ParcelListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs


class ParcelCreateView(LoginRequiredMixin, CreateView):
    template_name = 'common_form/create-and-update.html'
    form_class = ParcelForm
    success_url = '/parcels/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Created parcel')
        return super(ParcelCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ParcelCreateView, self).get_context_data(**kwargs)
        context["title"] = 'Create a Parcel'
        return context

    def get_form_kwargs(self):
        kwargs = super(ParcelCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ParcelUpdateView(LoginRequiredMixin, UpdateView):
    model = Parcel
    template_name = 'common_form/create-and-update.html'
    form_class = ParcelForm
    success_url = '/parcels/'

    def form_valid(self, form):
        messages.success(self.request, 'updated parcel')
        return super(ParcelUpdateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ParcelUpdateView, self).get_context_data(**kwargs)
        context["title"] = 'Update Parcel'
        return context

    def get_form_kwargs(self):
        kwargs = super(ParcelUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
