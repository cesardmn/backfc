from django.contrib import admin
from .models import *


def ativar(modeladmin, request, queryset):
    for item in queryset:
        item.active = True
        item.save()


def desativar(modeladmin, request, queryset):
    for item in queryset:
        item.active = False
        item.save()


@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'acompanhamentos',
        'carnes',
        'frangos',
        'massas',
        'peixe',
        'active'

    )

    actions = (
        ativar,
        desativar
    )


@admin.register(Fit)
class FitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'active'
    )

    list_display_links = (
        'name',
    )

    actions = (
        ativar,
        desativar
    )


@admin.register(LowCarb)
class LowCarbAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'active'
    )

    list_display_links = (
        'name',
    )

    actions = (
        ativar,
        desativar
    )


@admin.register(Portion)
class PortionAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'name',
        'price',
        'active'
    )

    list_display_links = (
        'name',
    )

    list_filter = (
        'type',
        'active'
    )

    actions = (
        ativar,
        desativar
    )
