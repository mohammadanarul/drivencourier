from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.location import Location
from ..forms.location import LocationForm


class LocationCreateAndListView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'location/list.html'


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    template_name = 'common_form/create-and-update.html'
    form_class = LocationForm
    success_url = '/locations/'

    def get_context_data(self, **kwargs):
        context = super(LocationCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create a Location'
        return context


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = Location
    template_name = 'common_form/create-and-update.html'
    form_class = LocationForm
    success_url = '/locations/'

    def get_context_data(self, **kwargs):
        context = super(LocationUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Location update'
        return context


class LocationDeleteView(LoginRequiredMixin, DeleteView):
    model = Location
    success_url = '/locations/'

