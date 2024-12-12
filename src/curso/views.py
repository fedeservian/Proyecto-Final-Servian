from django.shortcuts import redirect, render
from .forms import CategoryForm, ProductForm, ProductionOrderForm, InventoryForm
from .models import Category, Product, ProductionOrder, Inventory

def index(request):
    return render(request, "curso/index.html")

def about(request):
    return render(request, "curso/about.html")

def category_list(request):
    query = Category.objects.all()
    context = {"object_list": query}
    return render(request, "curso/category_list.html", context)

def category_create(request):
    if request.method == "GET":
        form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            return redirect("curso:category_list")
    return render(request, "curso/category_form.html", {"form": form})

def product_list(request):
    query = Product.objects.all()
    context = {"object_list": query}
    return render(request, "curso/product_list.html", context)

def product_create(request):
    if request.method == "GET":
        form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect("curso:product_list")
    return render(request, "curso/product_form.html", {"form": form})

def production_order_list(request):
    query = ProductionOrder.objects.all()
    context = {"object_list": query}
    return render(request, "curso/production_order_list.html", context)

def production_order_create(request):
    if request.method == "GET":
        form = ProductionOrderForm()
    if request.method == "POST":
        form = ProductionOrderForm(request.POST)
        if form.is_valid():
            return redirect("curso:production_order_list")
    return render(request, "curso/production_order_form.html", {"form": form})

def inventory_list(request):
    query = Inventory.objects.all()
    context = {"object_list": query}
    return render(request, "curso/inventory_list.html", context)

def inventory_create(request):
    if request.method == "GET":
        form = InventoryForm()
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            return redirect("curso:inventory_list")
    return render(request, "curso/inventory_form.html", {"form": form})


