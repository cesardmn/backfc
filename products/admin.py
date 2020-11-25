from django.contrib import admin
from django.forms.widgets import Textarea
from .models import *


def ativar(modeladmin, request, queryset):
    for item in queryset:
        item.active = True
        item.save()


def desativar(modeladmin, request, queryset):
    for item in queryset:
        item.active = False
        item.save()

def ativar_desconto(modeladmin, request, queryset):
    for item in queryset:
        item.discount = True
        item.save()

def desativar_desconto(modeladmin, request, queryset):
    for item in queryset:
        item.discount = False
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

    list_filter = ('active',)

    ordering = ('id',)

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
        'active',
        'discount'
    )

    list_display_links = ('id', 'name', 'price')

    list_filter = ('active', 'discount',)

    ordering = ('id',)

    actions = (ativar, desativar, ativar_desconto, desativar_desconto)

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 2, 'cols': 45})
        },
    }


@admin.register(LowCarb)
class LowCarbAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'active',
        'discount'
    )

    list_display_links = ('id', 'name', 'price')

    list_filter = ('active', 'discount',)

    ordering = ('id',)

    actions = (ativar, desativar, ativar_desconto, desativar_desconto)

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 2, 'cols': 45})
        },
    }


@admin.register(Portion)
class PortionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'name',
        'price',
        'active',
        'discount'
    )

    list_display_links = ('id', 'type','name', 'price')

    list_filter = ('type', 'active', 'discount',)

    ordering = ('id',)

    actions = (ativar, desativar, ativar_desconto, desativar_desconto)

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 2, 'cols': 45})
        },
    }
