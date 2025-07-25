from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import ActivatedCode, InviteCode, User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_per_page = 10
    list_display = (
        'phone_number',
        'first_name',
        'last_name',
        'invite_code',
        'has_activated_code',
    )
    search_fields = ('phone_number',)
    readonly_fields = ('has_activated_code',)

    def has_activated_code(self, obj):
        return obj.has_activated_code
    has_activated_code.short_description = 'Активировал код'
    has_activated_code.boolean = True


@admin.register(InviteCode)
class InviteCodeAdmin(ModelAdmin):
    list_per_page = 10
    list_display = ('user', 'code')
    search_fields = ('code',)


@admin.register(ActivatedCode)
class ActivatedCodeAdmin(ModelAdmin):
    list_per_page = 10
    list_display = ('user', 'code')
    search_fields = ('code',)
