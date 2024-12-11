from django.contrib import admin
from .models import Category, Product, ProductionOrder, Inventory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost_price', 'production_time', 'category')  
    search_fields = ('name', 'description')  

@admin.register(ProductionOrder)
class ProductionOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'product', 'status', 'quantity')  
    search_fields = ('order_number',)  

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'location', 'stock_quantity')  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  
    search_fields = ('name',)  

