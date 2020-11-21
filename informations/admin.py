from django.contrib import admin
from informations.models import *


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('info_one', 'info_two')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product', 'about', 'amount')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('whatsapp', 'instagram', 'email')


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('info_one', 'info_two')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('info_one', 'info_two')
