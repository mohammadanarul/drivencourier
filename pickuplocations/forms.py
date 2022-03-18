from django import forms
from .models import PickupLocation

class PicupLocationForm(forms.ModelForm):
    
    class Meta:
        model = PickupLocation
        fields = (
            "pickup_name",
            "pickup_address",
            "pickup_area",
            "pickup_phone_number",
            )
    def __init__(self, *args, **kwargs):
        super(PicupLocationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'