from django.contrib import admin
from .models import Repairs, Car, Client


# Register your models here.

admin.site.register(Repairs)
admin.site.register(Car)
admin.site.register(Client)

# admin.site.register(PersonMechanic)
