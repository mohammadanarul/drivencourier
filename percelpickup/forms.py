from django import forms
from .models import PercelPickup
from accounts.models import Rider


class PercelPickupForm(forms.ModelForm):
    class Meta:
        model = PercelPickup
        field = '__all__'
        exclude = ['pickuped_to', 'completed']
    
    def __init__(self, *args, **kwargs):
        super(PercelPickupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'