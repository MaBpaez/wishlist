from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from inventory.models import Product


class WishItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='wish_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    publish = models.DateTimeField("fecha de publicación", default=timezone.now)
    created = models.DateTimeField("fecha de creación", auto_now_add=True)
    updated = models.DateTimeField("fecha de modificación", auto_now=True)
