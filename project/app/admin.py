from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import InviteCode, User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_per_page = 10
    list_display = ('phone_number', 'first_name', 'last_name', 'invite_code')
    search_fields = ('phone_number',)


@admin.register(InviteCode)
class InviteCodeAdmin(ModelAdmin):
    list_per_page = 10
    list_display = ('user', 'code')
    search_fields = ('code',)
