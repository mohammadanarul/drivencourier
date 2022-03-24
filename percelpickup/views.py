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
from accounts.models import Rider

class PercelPickupCreateView(CreateView):
    form_class = PercelPickupForm
    template_name = "percelpickup/percel-pickup-created.html"

    def form_valid(self, form):
        form.instance.pickuped_to = self.request.user
        form.instance.percel.status = 'Processing'
        return super(PercelPickupCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        current_location = self.request.user.location
        kwargs['pickup_by'] = Rider.objects.filter(location=current_location)
        kwargs['percel'] = Percel.objects.filter(status="PickupPending")
        return super(PercelPickupCreateView, self).get_context_data(**kwargs)
