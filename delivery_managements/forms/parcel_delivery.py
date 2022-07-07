from django.forms import ModelForm
from accounts.models import Rider
from ..models.branch import Branch
from ..models.parcel import Parcel
from ..models.parcel_delivery import ParcelDelivery


class ParcelDeliveryForm(ModelForm):
    class Meta:
        model = ParcelDelivery
        fields = ('delivery_rider', 'parcel', 'status')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ParcelDeliveryForm, self).__init__(*args, **kwargs)
        branch = Branch.objects.get(user=self.request.user)
        self.fields['delivery_rider'].queryset = Rider.objects.filter(branch=branch)
        self.fields['parcel'].queryset = Parcel.objects.filter(delivery_location=branch)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'

