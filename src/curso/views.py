from django.shortcuts import redirect, render
from .forms import CategoryForm, ProductForm, ProductionOrderForm, InventoryForm
from .models import Category, Product, ProductionOrder, Inventory
from .forms import CustomAuthenticationForm, CustomCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from django.forms import ModelForm



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

 
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'curso/login.html'
    next_page = reverse_lazy('curso:index')

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        usuario = form.get_user()
        messages.success(self.request, f"Login Successful, ¡Welcome {usuario.username}!")
        return super().form_valid(form)
    
class CustomRegisterView(CreateView):
    form_class = CustomCreationForm
    template_name = 'curso/register.html'
    
    
    def get_success_url(self):
        return reverse_lazy('curso:login')  

    def form_valid(self, form):
        messages.success(self.request, "¡Registered Successfully! Your account has been created. Now login to access your profile.")
        return super().form_valid(form)