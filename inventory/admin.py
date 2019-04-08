from django.contrib import admin

# Register your models here.
from.models import Inventory_Records, User

admin.site.register(Inventory_Records)

admin.site.register(User)