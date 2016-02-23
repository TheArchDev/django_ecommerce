from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import Product, Order, UserProfile

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(UserProfile)