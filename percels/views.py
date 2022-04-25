from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView
)
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Percel
from .forms import PercelForm
from percelpickup.models import PercelPickup

class HomeView(TemplateView):
    template_name = "landing.html"

class DashboardView(LoginRequiredMixin, ListView):
    model = Percel
    template_name = 'dashboard.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(DashboardView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs
    
    def get_context_data(self, **kwargs):
        context =  super(DashboardView, self).get_context_data(**kwargs)
        context["pickup_percel_list"] = PercelPickup.objects.filter(status='Pending')
        context["percel_pickup_manager_accepted"] = PercelPickup.objects.filter(status='Accept')
        return context

class PercelListView(LoginRequiredMixin, ListView):
    model = Percel
    template_name = "percels/percel-list.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(PercelListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs


class PercelCreateView(LoginRequiredMixin, CreateView):
    template_name = 'percels/create_and_update_percel.html'
    form_class = PercelForm
    success_url = reverse_lazy('percels:percels_view')

    def form_valid(self, form):
        # You need to get a new object based on the form
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        ... # in case you want to modify the object before commit
        self.object.save()
        # you can use it to assign to the second model
        PercelPickup.objects.create(percel=self.object)
        messages.success(self.request, 'Created percel')
        return super(PercelCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        kwargs['pickup_location'] = self.request.user.pickup_location.all()
        context =  super(PercelCreateView, self).get_context_data(**kwargs)
        context["title"] = 'Create Percel'
        return context


class PercelUpdateView(LoginRequiredMixin, UpdateView):
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

