from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account, Customer, Manager, Rider

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Account
        fields = ['username', 'email', 'type', 'is_staff']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'phone_number', 'type', 'is_staff']


class CustomerRegisterForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = [
            'username',
            'email',
            'phone_number',
            'gender',
            'location',
            'address',
            'password1',
            'password2'
        ]

        def clean_email(self):
            email = self.cleaned_data["email"].lower()
            try:
                email = Account.objects.get(email=email)
            except Exception as e:
                return email
            raise forms.ValueError(f'email {self.email} is Alredy used.')

        def clean_email(self):
            phone_number = self.cleaned_data["phone_number"].lower()
            try:
                phone_number = Account.objects.get(phone_number=phone_number)
            except Exception as e:
                return phone_number
            raise forms.ValueError(f'phone_number {self.phone_number} is Alredy used.')
        
        def clean_username(self):
            username = self.cleaned_data["username"]
            try:
                username = Account.objects.get(username=username)
            except Exception as e:
                return username
            raise forms.ValueError(f'username {self.username} is Alredy used.')

    def __init__(self, *args, **kwargs):
        super(CustomerRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'

class ManagerRegisterForm(UserCreationForm):
    class Meta:
        model = Manager
        fields = [
            'username',
            'email',
            'phone_number',
            'gender',
            'location',
            'address',
            'password1',
            'password2'
        ]

        def clean_email(self):
            email = self.cleaned_data["email"].lower()
            try:
                email = Account.objects.get(email=email)
            except Exception as e:
                return email
            raise forms.ValueError(f'email {self.email} is Alredy used.')

        def clean_email(self):
            phone_number = self.cleaned_data["phone_number"].lower()
            try:
                phone_number = Account.objects.get(phone_number=phone_number)
            except Exception as e:
                return phone_number
            raise forms.ValueError(f'phone_number {self.phone_number} is Alredy used.')
        
        def clean_username(self):
            username = self.cleaned_data["username"]
            try:
                username = Account.objects.get(username=username)
            except Exception as e:
                return username
            raise forms.ValueError(f'username {self.username} is Alredy used.')

    def __init__(self, *args, **kwargs):
        super(ManagerRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'

class RiderRegisterForm(UserCreationForm):
    class Meta:
        model = Rider
        fields = [
            'username',
            'email',
            'phone_number',
            'gender',
            'location',
            'address',
            'password1',
            'password2'
        ]

        def clean_email(self):
            email = self.cleaned_data["email"].lower()
            try:
                email = Account.objects.get(email=email)
            except Exception as e:
                return email
            raise forms.ValueError(f'email {self.email} is Alredy used.')

        def clean_email(self):
            phone_number = self.cleaned_data["phone_number"].lower()
            try:
                phone_number = Account.objects.get(phone_number=phone_number)
            except Exception as e:
                return phone_number
            raise forms.ValueError(f'phone_number {self.phone_number} is Alredy used.')
        
        def clean_username(self):
            username = self.cleaned_data["username"]
            try:
                username = Account.objects.get(username=username)
            except Exception as e:
                return username
            raise forms.ValueError(f'username {self.username} is Alredy used.')

    def __init__(self, *args, **kwargs):
        super(RiderRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'