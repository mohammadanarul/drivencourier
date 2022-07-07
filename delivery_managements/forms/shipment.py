from django.forms import ModelForm
from ..models.shipment import Shipment


class ShipmentForm(ModelForm):
    class Meta:
        model = Shipment
        fields = '__all__'
        exclude = ('shipment_to', 'sender_branch', 'created_at', 'updated_at')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ShipmentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
