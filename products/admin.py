from django.contrib import admin
import locale
from django.forms.widgets import Textarea
from .models import Combo, Fit, Item, ItemGroup, ItemType, LowCarb, Portion


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


@admin.register(ItemGroup)
class ItemGroupAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'package')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'active',
        'description',
        'type',
        'group',
        'full_price_format',
        'sale_price_format',
        'discount',
    )

    list_display_links = ('id', 'description')

    ordering = ('group', 'type', 'id')

    actions = (ativar, desativar, ativar_desconto, desativar_desconto)

    list_filter = ('group', 'type', 'active')

    search_fields = ('description', )

    def full_price_format(self, obj):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(obj.full_price)
    full_price_format.short_description = 'preço cheio'

    def sale_price_format(self, obj):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(obj.sale_price)
    sale_price_format.short_description = 'preço de venda'
