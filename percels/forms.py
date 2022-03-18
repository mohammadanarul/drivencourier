from django import forms
from .models import Percel

class PercelForm(forms.ModelForm):
    class Meta:
        model = Percel
        fields = (
            "customer_name",
            "customer_phone_number",
            "customer_address",
            'pickup_location',
            "parcel_weight",
            "delivery_location",
            "product_selling_price",
            "product_category",
            'description',
        )
    def __init__(self, *args, **kwargs):
        super(PercelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'