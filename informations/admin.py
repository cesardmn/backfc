from django.contrib import admin
from informations.models import *

admin.site.register(About)
admin.site.register(Products)
admin.site.register(Contact)
admin.site.register(Delivery)
admin.site.register(Order)

admin.site.site_header = 'Fogão Caseiro - admin'