from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from candies.models import Candy


class CandyResource(resources.ModelResource):
    class Meta:
        model = Candy
        fields = [
            'id',
            'name',
            'name_en',
            'name_de',
            'name_th',
            'name_cn',
            'description',
            'description_en',
            'description_de',
            'description_th',
            'description_cn',
        ]


class CandyAdmin(ImportExportModelAdmin):
    resource_class = CandyResource


admin.site.register(Candy, CandyAdmin)
