from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_per_page = 10
    list_display = ('phone_number', 'first_name', 'last_name',)
    search_fields = ('phone_number',)
