from django.contrib import admin

from shipper.models import Cargo, Order

admin.site.register(Order)
admin.site.register(Cargo)
