from django.contrib import admin

from fauzans.models import Fauzan


class FauzanAdmin(admin.ModelAdmin):
    __basic_fields = ['id', 'name', 'last_name']
    list_display = __basic_fields
    list_display_links = __basic_fields


admin.site.register(Fauzan, FauzanAdmin)
