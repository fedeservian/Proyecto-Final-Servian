from django.shortcuts import redirect, render
from .forms import CategoryForm, ProductForm, ProductionOrderForm, InventoryForm
from .models import Category, Product, ProductionOrder, Inventory
from .forms import CustomAuthenticationForm, CustomCreationForm, UserProfileForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest




def index(request):
    return render(request, "curso/index.html")

def about(request):
    return render(request, "curso/about.html")

@login_required
def category_list(request: HttpResponse) -> HttpResponse:
    search_query = request.GET.get('search')
    if search_query:
        queryset = Category.objects.filter(name__icontains=search_query)
    else:
        queryset = Category.objects.all()
    context = {"object_list": queryset, 'search_query': search_query}
    return render(request, "curso/category_list.html", context)


def category_create(request):
    if request.method == "GET":
        form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso:category_list")
    return render(request, "curso/category_form.html", {"form": form})


# Categoria UPDATE VIEW
def category_update(request, pk: int):
    query = Category.objects.get(id=pk)
    if request.method == "GET":
        form = CategoryForm(instance=query)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("curso:category_list")
    return render(request, "curso/category_form.html", {"form": form})

def category_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Category.objects.get(id=pk)
    return render(request, 'curso/category_detail.html', {'object': query})

def category_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Category.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('curso:category_list')
    return render(request, 'curso/category_confirm_delete.html', {'object': query})

@login_required
def product_list(request: HttpResponse) -> HttpResponse:
    search_query = request.GET.get('search')
    if search_query:
        queryset = Product.objects.filter(name__icontains=search_query)
    else:
        queryset = Product.objects.all()
    context = {"object_list": queryset, 'search_query': search_query}
    return render(request, "curso/product_list.html", context)


def product_create(request):
    if request.method == "GET":
        form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso:product_list")
    return render(request, "curso/product_form.html", {"form": form})

def product_update(request, pk: int):
    query = Product.objects.get(id=pk)
    if request.method == "GET":
        form = ProductForm(instance=query)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("curso:product_list")
    return render(request, "curso/product_form.html", {"form": form})

def product_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Product.objects.get(id=pk)
    return render(request, 'curso/product_detail.html', {'object': query})

def product_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Product.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('curso:product_list')
    return render(request, 'curso/product_confirm_delete.html', {'object': query})

@login_required
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
            form.save()
            return redirect("curso:production_order_list")
    return render(request, "curso/production_order_form.html", {"form": form})

def production_order_update(request, pk: int):
    query = ProductionOrder.objects.get(id=pk)
    if request.method == "GET":
        form = ProductionOrderForm(instance=query)
    if request.method == "POST":
        form = ProductionOrderForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("curso:production_order_list")
    return render(request, "curso/production_order_form.html", {"form": form})

def production_order_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = ProductionOrder.objects.get(id=pk)
    return render(request, 'curso/production_order_detail.html', {'object': query})

def production_order_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = ProductionOrder.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('curso:production_order_list')
    return render(request, 'curso/producttion_order_confirm_delete.html', {'object': query})

@login_required
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
            form.save()
            return redirect("curso:inventory_list")
    return render(request, "curso/inventory_form.html", {"form": form})

def inventory_update(request, pk: int):
    query = Inventory.objects.get(id=pk)
    if request.method == "GET":
        form = InventoryForm(instance=query)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("curso:inventory_list")
    return render(request, "curso/inventory_form.html", {"form": form})

def inventory_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = Inventory.objects.get(id=pk)
    return render(request, 'curso/inventory_detail.html', {'object': query})

def inventory_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('curso:inventory_list')
    return render(request, 'curso/inventory_confirm_delete.html', {'object': query})

 
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
    
class UpdateProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'curso/profile.html'
    success_url = reverse_lazy('curso:index')

    def get_object(self):
        return self.request.user