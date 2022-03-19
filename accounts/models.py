from django.db import models
from django.db.models import Q
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
    )
from multiselectfield import MultiSelectField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.urls import reverse
from .managers import AccountManager
from locations.models import Location

# Custom user created.
class Account(AbstractBaseUser, PermissionsMixin):
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    class UserTypes(models.TextChoices):
        MANAGER                 = 'MANAGER', 'Manager'
        RIDER                   = 'RIDER', 'Rider'
        CUSTOMER                = 'CUSTOMER', 'Customer'
    
    default_type = UserTypes.CUSTOMER

    phone_regex             = RegexValidator(regex=r'^(((?:\+88)?(?:\d{11}))|((?:01)?(?:\d{11})))$',
                                             message='Phone number must be entred in the format: +8801555555550, Up to 11 digits allowed.')
    type                    = MultiSelectField(choices=UserTypes.choices, default=[], null=True, blank=True)
    username                = models.CharField(max_length=155, unique=True, blank=True)
    email                   = models.EmailField(unique=True, blank=True)
    phone_number            = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    gender                  = models.CharField(_("gender"), choices=GENDER_CHOICES, max_length=6)
    location                = models.ForeignKey(Location, on_delete=models.SET_NULL, verbose_name=('location'), null=True, blank=True)
    address                 = models.CharField(_('address'), max_length=50)
    otp                     = models.CharField(_("otp"), max_length=6, blank=True)
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    joinded_date            = models.DateTimeField(verbose_name='date join', auto_now_add=True)
    is_active               = models.BooleanField(default=True)
    is_admin                = models.BooleanField(default=False)
    is_staff                = models.BooleanField(default=False)
    
    objects = AccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return f'{self.username}'    
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        #Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        #Simplest possible answer: Yes, always
        return True
    
    def get_absolute_url(self):
        return reverse('accounts:dashboard_view', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.type.append(self.default_type)
        return super().save(*args, **kwargs)


# Accounts query managers
class AreaManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = Account.UserTypes.MANAGER))

class RiderManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = Account.UserTypes.RIDER))

class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = Account.UserTypes.CUSTOMER))


class Manager(Account):
    default_type = Account.UserTypes.MANAGER
    objects = AreaManager()

    class Meta:
        proxy = True


class Rider(Account):
    default_type = Account.UserTypes.RIDER
    objects = RiderManager()

    class Meta:
        proxy = True


class Customer(Account):
    default_type = Account.UserTypes.CUSTOMER
    objects = CustomerManager()
    
    class Meta:
        proxy = True