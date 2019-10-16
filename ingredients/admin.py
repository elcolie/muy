from django.contrib import admin

from ingredients.models import Category, Ingredient


class CategoryAdmin(admin.ModelAdmin):
    __basic_fields = ['id', 'name']
    list_display = __basic_fields
    list_display_links = __basic_fields


class IngredientAdmin(admin.ModelAdmin):
    __basic_fields = [
        'name',
        'notes',
        'category',
    ]
    list_display = __basic_fields
    list_display_links = __basic_fields


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
