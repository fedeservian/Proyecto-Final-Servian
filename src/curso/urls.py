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

    path("category/update/<int:pk>/", views.category_update, name="category_update"),
    path("product/update/<int:pk>/", views.product_update, name="product_update"),
    path("production_order/update/<int:pk>/", views.production_order_update, name="production_order_update"),
    path("inventory/update/<int:pk>/", views.inventory_update, name="inventory_update"),

    path("category/detail/<int:pk>/", views.category_detail, name="category_detail"),
    path("product/detail/<int:pk>/", views.product_detail, name="product_detail"),
    path("production_order/detail/<int:pk>/", views.production_order_detail, name="production_order_detail"),
    path("inventory/detail/<int:pk>/", views.inventory_detail, name="inventory_detail"),
    
    path("product/list/", product_list, name="product_list"),
    path("product/create/", product_create, name="product_create"),

    path("production_order/list/", production_order_list, name="production_order_list"),
    path("production_order/create/", production_order_create, name="production_order_create"),

    path("inventory/list/", inventory_list, name="inventory_list"),
    path("inventory/create/", inventory_create, name="inventory_create"),

    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='curso/logout.html'), name='logout'),
    path('register/', views.CustomRegisterView.as_view(), name='register' ),
    path('profile/', views.UpdateProfileView.as_view(), name='profile'),
]