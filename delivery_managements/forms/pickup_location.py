from django.forms import ModelForm
from ..models.pickup_location import PickupLocation


class PicupLocationForm(ModelForm):
    
    class Meta:
        model = PickupLocation
        fields = (
            "pickup_name",
            "pickup_address",
            "branch",
            "pickup_phone_number",
            )

    def __init__(self, *args, **kwargs):
        super(PicupLocationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
