from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from ..models.branch import Branch
from ..models.parcel_picup import ParcelPickup
from ..forms.parcel_pickup import ParcelPickupForm


class ParcelPickupListView(LoginRequiredMixin, ListView):
    model = ParcelPickup
    template_name = 'parcel_pickup/list.html'
    success_url = reverse_lazy('parcel_pickup_list_view')


class ParcelPickupCreateView(LoginRequiredMixin, CreateView):
    model = ParcelPickup
    form_class = ParcelPickupForm
    template_name = 'common_form/create-and-update.html'
    success_url = reverse_lazy('parcel_pickup_list_view')

    def form_valid(self, form):
        form1 = form.save(commit=False)
        form1.pickup_to = self.request.user
        form1.save()
        print(self.request.POST.getlist('parcel'))
        form.save_m2m()
        return super(ParcelPickupCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Parcel Pickup'
        return context

    def get_form_kwargs(self):
        kwargs = super(ParcelPickupCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ParcelPickupUpdateView(LoginRequiredMixin, UpdateView):
    model = ParcelPickup
    form_class = ParcelPickupForm
    template_name = 'common_form/create-and-update.html'
    success_url = reverse_lazy('parcel_pickup_list_view')

    def form_valid(self, form):
        form1 = form.save(commit=False)
        form1.pickup_to = self.request.user
        form1.save()
        form.save_m2m()
        return super(ParcelPickupUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Update Parcel Pickup'
        return context

    def get_form_kwargs(self):
        kwargs = super(ParcelPickupUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ParcelPickupDeleteView(LoginRequiredMixin, DeleteView):
    model = ParcelPickup
    success_url = reverse_lazy('parcel_pickup_list_view')
