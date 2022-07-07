from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.parcel_delivery import ParcelDelivery
from ..forms.parcel_delivery import ParcelDeliveryForm


class ParcelDeliveryListView(LoginRequiredMixin, ListView):
    model = ParcelDelivery
    template_name = 'parcel_delivery/list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(ParcelDeliveryListView, self).get_queryset(*args, **kwargs)
        return qs.filter(delivery_to=self.request.user)


class ParcelDeliveryCreateView(LoginRequiredMixin, CreateView):
    form_class = ParcelDeliveryForm
    template_name = "common_form/create-and-update.html"
    success_url = reverse_lazy('parcel_delivery_list_view')

    def form_valid(self, form):
        form.instance.delivery_to = self.request.user
        return super(ParcelDeliveryCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ParcelDeliveryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Parcel Delivery Create.'
        return context

    def get_form_kwargs(self):
        kwargs = super(ParcelDeliveryCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ParcelDeliveryUpdateView(LoginRequiredMixin, UpdateView):
    model = ParcelDelivery
    form_class = ParcelDeliveryForm
    template_name = "common_form/create-and-update.html"
    success_url = reverse_lazy('parcel_delivery_list_view')

    def get_context_data(self, **kwargs):
        context = super(ParcelDeliveryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Parcel Delivery update.'
        return context

    def get_form_kwargs(self):
        kwargs = super(ParcelDeliveryUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ParcelDeliveryDeleteView(LoginRequiredMixin, DeleteView):
    model = ParcelDelivery
    success_url = reverse_lazy('parcel_delivery_list_view')


