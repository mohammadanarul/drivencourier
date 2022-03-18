from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, ReadOnlyPasswordHashWidget
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)
from .models import (
    Account,
    Manager,
    Customer,
    Rider
)


@admin.register(Account)
class UserAccountModelAdmin(UserAdmin):
    list_display = ('username', 'phone_number', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('phone_number', 'username', 'joinded_date')
    readonly_fields = ('pk', 'joinded_date', 'last_login')
    filter_horizontal = []
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'type', 'password1', 'password2')}
        ),
    )


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('__all__',)}
        ),
    )
    readonly_fields = ('pk', 'joinded_date', 'last_login')
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('__all__',)}
        ),
    )
    readonly_fields = ('pk', 'joinded_date', 'last_login')

@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('__all__',)}
        ),
    )
    readonly_fields = ('pk', 'joinded_date', 'last_login')