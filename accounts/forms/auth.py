from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CheckboxInput
from ..models import Account


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Account
        fields = ['username', 'email', 'phone_number', 'type', 'is_staff']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = '__all__'


class AccountForm(UserCreationForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'email',
            'phone_number',
            'gender',
            'address',
            'branch',
            'type'
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
        super(AccountForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                'class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'


class AccountUpdateForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'email',
            'phone_number',
            'gender',
            'address',
            'branch',
            'type',
            'is_active'
        ]

    def __init__(self, *args, **kwargs):
        super(AccountUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                'class'] = 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
            self.fields['is_active'].widget = CheckboxInput(attrs={'class': 'text-purple-600 form-radio focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray ml-3'})