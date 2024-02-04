from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created', 'updated')
