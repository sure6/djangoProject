from django.contrib import admin
from .models import RentModel, Bill

# Register your models here.
admin.site.register(RentModel)
admin.site.register(Bill)