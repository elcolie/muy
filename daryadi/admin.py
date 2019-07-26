from django.contrib import admin

from daryadi.models import PuzzleMoney


class PuzzleMoneyAdmin(admin.ModelAdmin):
    pass


admin.site.register(PuzzleMoney, PuzzleMoneyAdmin)
