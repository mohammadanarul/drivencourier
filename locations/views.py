from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import View, CreateView, ListView
from django.urls import reverse_lazy
from django.conf import settings
from accounts.views import HubManagerRequiredMixin

from .forms import LocationForm

from .models import Location

# class LocationListview(HubManagerRequiredMixin, ListView):
#     model = Location
#     template_name = 'percels/arealocation-list.html'

# class LocationCreateView(HubManagerRequiredMixin, CreateView):
#     model = Location
#     template_name = 'percels/create_arealocation.html'
#     form_class = LocationForm 
#     success_url = reverse_lazy('percel:home_page')

