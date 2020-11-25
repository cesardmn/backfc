from django.contrib import admin
from informations.models import *
from django.forms import TextInput, Textarea


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('info_one', 'info_two')
    list_display_links = ('info_one', 'info_two')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 45})},
    }


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product', 'about', 'amount')
    list_display_links = ('product', 'about', 'amount')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 30})},
    }


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('whatsapp', 'instagram', 'email')
    list_display_links = ('whatsapp', 'instagram', 'email')


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('info_one', 'info_two')
    list_display_links = ('info_one', 'info_two')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 30})},
    }

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('info_one', 'info_two')
    list_display_links = ('info_one', 'info_two')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 25})},
    }
