from django.contrib import admin
from .models import Percel

@admin.register(Percel)
class PercelAdmin(admin.ModelAdmin):
    list_display = ['user', 'customer_name', 'pickuplocation']
