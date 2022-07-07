from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils.translation import gettext_lazy as _
# from django.urls import reverse

from delivery_managements.models.branch import Branch
from .managers import UserManager

phone_regex = RegexValidator(regex=r'^(((?:\+88)?(?:\d{11}))|((?:01)?(?:\d{11})))$',
                             message='Phone number must be entered in the format: +8801555555550, '
                                     'Up to 11 digits allowed.')


# Custom user created.
class Account(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    class UserTypes(models.TextChoices):
        RIDER = 'RIDER', 'Rider'
        MERCHANT = 'MERCHANT', 'Merchant'

    default_type = UserTypes.MERCHANT
    type = models.CharField(_("Type"), max_length=50, choices=UserTypes.choices, default=default_type,
                            db_index=True)
    username = models.CharField(max_length=155, unique=True, blank=True, db_index=True,)
    email = models.EmailField(unique=True, blank=True, db_index=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=14,
                                    unique=True, db_index=True)
    gender = models.CharField(_("gender"), choices=GENDER_CHOICES, max_length=6, db_index=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    address = models.CharField(_('address'), max_length=50)
    otp = models.CharField(_("otp"), max_length=6, blank=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return f'{self.username}'

    @property
    def user_rider(self):
        return self.UserTypes.RIDER

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

    # def get_absolute_url(self):
    #     return reverse('accounts:dashboard_view', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.default_type
        return super().save(*args, **kwargs)


# managers
class MerchantManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.UserTypes.MERCHANT)


class RiderManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Account.UserTypes.RIDER)


class Merchant(Account):
    default_type = Account.UserTypes.MERCHANT
    objects = MerchantManager()

    class Meta:
        proxy = True


class Rider(Account):
    default_type = Account.UserTypes.RIDER
    objects = RiderManager()

    class Meta:
        proxy = True
