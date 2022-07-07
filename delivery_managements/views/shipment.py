from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models.branch import Branch
from ..models.shipment import Shipment
from ..forms.shipment import ShipmentForm


class ShipmentListView(LoginRequiredMixin, ListView):
    model = Shipment
    template_name = 'shipment/list.html'

    def get_queryset(self, **kwargs):
        qs = super(ShipmentListView, self).get_queryset(**kwargs)
        return qs.filter(shipment_to=self.request.user)


class ShipmentCreateView(CreateView):
    model = Shipment
    form_class = ShipmentForm
    template_name = 'common_form/create-and-update.html'
    success_url = reverse_lazy('shipment_list_view')

    def form_valid(self, form):
        branch = Branch.objects.get(user=self.request.user)
        form1 = form.save(commit=False)
        form1.shipment_to = self.request.user
        form1.sender_branch = branch
        form1.save()
        form.save_m2m()
        return super(ShipmentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ShipmentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Shipment Delivery Create'
        return context

    def get_form_kwargs(self):
        kwargs = super(ShipmentCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ShipmentUpdateView(UpdateView):
    model = Shipment
    form_class = ShipmentForm
    template_name = 'common_form/create-and-update.html'
    success_url = reverse_lazy('shipment_list_view')

    def form_valid(self, form):
        branch = Branch.objects.get(user=self.request.user)
        form1 = form.save(commit=False)
        form1.shipment_to = self.request.user
        form1.sender_branch = branch
        form.save_m2m()
        return super(ShipmentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ShipmentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Shipment Delivery Update'
        return context

    def get_form_kwargs(self):
        kwargs = super(ShipmentUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ShipmentDeleteView(DeleteView):
    model = Shipment
    success_url = reverse_lazy('shipment_list_view')

