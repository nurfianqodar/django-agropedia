from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    readonly_fields = ['date_joined', 'last_login']

admin.site.register(Account, AccountAdmin)
