from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from ..models import Rider, Account


class RiderRegisterForm(UserCreationForm):
    class Meta:
        model = Rider
        fields = [
            'username',
            'email',
            'phone_number',
            'gender',
            'address',
            'password1',
            'password2'
        ]

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            username = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise ValidationError(f'Username {username} is already used')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            email = Account.objects.get(email=email).lower()
        except Exception as e:
            return email
        raise ValidationError(f'Username {email} is already used')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        try:
            phone_number = Account.objects.get(phone_number=phone_number)
        except Exception as e:
            return phone_number
        raise ValidationError(f'Username {phone_number} is already used')

    def __init__(self, *args, **kwargs):
        super(RiderRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                'class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
