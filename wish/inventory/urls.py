from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path("lista-de-productos/", views.products_list, name="products_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:product>/",
        views.product_detail,
        name="product_detail",
    ),
]
