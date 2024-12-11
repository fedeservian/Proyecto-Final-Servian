from django.shortcuts import render

from .models import Category, Product, ProductionOrder, Inventory

def index(request):
    return render(request, "curso/index.html")

def about(request):
    return render(request, "curso/about.html")

def category_list(request):
    query = Category.objects.all()
    context = {"object_list": query}
    return render(request, "curso/category_list.html", context)

def product_list(request):
    query = Product.objects.all()
    context = {"object_list": query}
    return render(request, "curso/product_list.html", context)

def production_order_list(request):
    query = ProductionOrder.objects.all()
    context = {"object_list": query}
    return render(request, "curso/production_order_list.html", context)

def inventory_list(request):
    query = Inventory.objects.all()
    context = {"object_list": query}
    return render(request, "curso/inventory_list.html", context)


