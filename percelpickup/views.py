from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)
from .forms import PercelPickupForm
from .models import PercelPickup
from percels.models import Percel
from pickuplocations.models import PickupLocation
from perceldelivery.models import PercelDelivery
from accounts.models import Rider
from django.urls import reverse_lazy, reverse

class PercelPickupCreateView(CreateView):
    form_class = PercelPickupForm
    template_name = "percelpickup/percel-pickup-created.html"
    success_url = reverse_lazy('percels:dashboard_view')

    def form_valid(self, form):
        form.instance.pickuped_to = self.request.user
        form.instance.percel.status = 'Processing'
        return super(PercelPickupCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        current_location = self.request.user.location
        kwargs['pickup_by'] = Rider.objects.filter(location=current_location)
        kwargs['percel'] = Percel.objects.filter(status="PickupPending")
        return super(PercelPickupCreateView, self).get_context_data(**kwargs)

def percel_pickup_accept(request, pk):
    current_rider = request.user
    pickup_percel = PercelPickup.objects.get(pk=pk, status='Pending')
    pickup_percel.status = 'Accept'
    pickup_percel.pickup_by = current_rider
    pickup_percel.save()
    return redirect(reverse('percels:dashboard_view'))


def percel_pickup_completed(request, pk):
    if request.user.user_manager:
        current_manager = request.user
        pickup_percel = PercelPickup.objects.get(pk=pk, status='Accept')
        pickup_percel.status = 'Completed'
        pickup_percel.pickuped_to = current_manager
        pickup_percel.save()
        PercelDelivery.objects.create(percel=pickup_percel.percel)
        return redirect(reverse('percels:dashboard_view'))
    else:
        print('Invalid user.....')

# class PercelPickupAcceptedView(UpdateView):
#     model = PercelPickup
#     fields = 'status'
#     success_url = reverse_lazy('percels:dashboard_view')

#     def form_valid(self, form):
#         form.instance.status = 'Accept'
#         return super(PercelPickupAcceptedView, self).form_valid(form)
