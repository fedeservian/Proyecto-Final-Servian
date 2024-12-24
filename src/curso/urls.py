from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import index, about, category_list, product_list, production_order_list, inventory_list, category_create, product_create, production_order_create, inventory_create

app_name = "curso"

urlpatterns = [
    path("", index, name="index"),
    path("about/", views.about, name="about"),
    path("category/list/", category_list, name="category_list"),
    path("category/create/", category_create, name="category_create"),
    
    path("product/list/", product_list, name="product_list"),
    path("product/create/", product_create, name="product_create"),

    path("production_order/list/", production_order_list, name="production_order_list"),
    path("production_order/create/", production_order_create, name="production_order_create"),

    path("inventory/list/", inventory_list, name="inventory_list"),
    path("inventory/create/", inventory_create, name="inventory_create"),

    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='curso/logout.html'), name='logout'),
    path('register/', views.CustomRegisterView.as_view(), name='register' ),
]