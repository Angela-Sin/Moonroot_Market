from django.contrib import admin

from .models import Ritual


@admin.register(Ritual)
class RitualAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
