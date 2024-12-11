from django.urls import path
from .views import index, about, category_list, product_list, production_order_list, inventory_list

app_name = "curso"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("category/list/", category_list, name="category_list"),
    path("product/list/", product_list, name="product_list"),
    path("production_order/list/", production_order_list, name="production_order_list"),
    path("inventory/list/", inventory_list, name="inventory_list"),
]