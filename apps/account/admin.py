from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.account.models import Notification, Account, AccountInfo


@admin.register(Account)
class AccountAdmin(UserAdmin):
    search_fields = ("phone",)
    list_display = ("username", "phone", "is_active")
    list_filter = ("role", "is_active")
    fieldsets = (
        (None, {
            "fields": ("first_name", "last_name", "username", "phone", "email", "password")
        }
         ),
        ("Permissions", {
            "fields": ("user_permissions", "groups", "is_superuser", "is_staff")
        }
         ),
        ("Importand Date", {
            "fields": ("last_login",)
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'), }),)
    readonly_fields = ("password", "last_login")


@admin.register(AccountInfo)
class AccountInfoAdmin(admin.ModelAdmin):
    list_display = ("bio", "profession", "is_visible", "account")
    list_filter = ("is_visible",)
    autocomplete_fields = ("technologies",)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("account", "type", "is_read", "message")
    list_filter = ("type", "is_read")
