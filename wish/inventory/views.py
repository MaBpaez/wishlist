from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from .models import Product
from wishlist.models import WishItem


def products_list(request):
    object_list = Product.objects.all()

    return render(request, 'inventory/products_list.html', {'products': object_list})


def product_detail(request, year, month, day, product):
    user = authenticate(username="Currito", password="gatunopersa")

    # print(user)
    product = get_object_or_404(
        Product,
        slug=product,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    if (
        user.is_authenticated
        and user.is_active
        and not user.is_staff
        and not user.is_superuser
    ):
        WishItem.objects.create(user=user, product=product)

    return render(
        request, 'inventory/product_detail.html', {'usuario': user, 'product': product}
    )
