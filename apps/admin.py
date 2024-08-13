from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Product, User


@admin.register(User)
class UserModel(ModelAdmin):
    pass


@admin.register(Product)
class ProductModel(ModelAdmin):
    pass
