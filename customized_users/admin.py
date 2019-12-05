from django.contrib import admin

from customized_users.models import User


class CustimizedUserAdmin(admin.ModelAdmin):
    __basic_fields = ['cognito_id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']
    list_display = __basic_fields
    list_display_links = __basic_fields


admin.site.register(User, CustimizedUserAdmin)
