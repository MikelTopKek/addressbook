from django.contrib import admin

from .models import People, Address

admin.site.register(People)
admin.site.register(Address)
