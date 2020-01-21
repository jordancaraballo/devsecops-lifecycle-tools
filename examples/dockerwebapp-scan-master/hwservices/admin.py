from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Manufacturer, Brand, Model

admin.site.register(Manufacturer)
admin.site.register(Brand)
admin.site.register(Model)
