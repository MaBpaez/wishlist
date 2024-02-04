from django.contrib import admin
from .models import WishItem


@admin.register(WishItem)
class WishListItemAdmin(admin.ModelAdmin):
    # list_display = ['user', 'product', 'publish']
    readonly_fields = ('created', 'updated')