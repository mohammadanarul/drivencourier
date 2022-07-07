from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms.auth import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)
from .models import Account, Rider, Merchant


@admin.register(Account)
class UserAccountModelAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'phone_number', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('phone_number', 'username', 'date_joined')
    readonly_fields = ('pk', 'date_joined', 'last_login')
    filter_horizontal = []
    model = Account
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'type', 'password1', 'password2'),
        }),
    )

    
@admin.register(Merchant)
class CustomerAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('__all__',)
        }),
    )
    readonly_fields = ('pk', 'date_joined', 'last_login')


@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('__all__',)
        }),
    )
    readonly_fields = ('pk', 'date_joined', 'last_login')
