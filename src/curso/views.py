from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CategoryForm, ProductForm, ProductionOrderForm, InventoryForm, CustomAuthenticationForm, CustomCreationForm, UserProfileForm
from .models import Category, Product, ProductionOrder, Inventory




def index(request):
    return render(request, "curso/index.html")

def about(request):
    return render(request, "curso/about.html")

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category

@login_required
def category_list(request: HttpResponse) -> HttpResponse:
    search_query = request.GET.get('search')
    queryset = Category.objects.filter(user=request.user)
    if search_query:
        queryset = queryset.filter(name__icontains=search_query)
    context = {
        "object_list": queryset,  
        'search_query': search_query
    }
    return render(request, "curso/category_list.html", context)



@login_required
def category_create(request):
    if request.method == "GET":
        form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)  
            category.user = request.user  
            category.save()  
            return redirect("curso:category_list")
    return render(request, "curso/category_form.html", {"form": form})


@login_required
def category_update(request, pk: int):
    query = get_object_or_404(Category, id=pk, user=request.user)  
    form = CategoryForm(instance=query)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("curso:category_list")
    return render(request, "curso/category_form.html", {"form": form})

@login_required
def category_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = get_object_or_404(Category, id=pk, user=request.user)  
    return render(request, 'curso/category_detail.html', {'object': query})


@login_required
def category_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = get_object_or_404(Category, id=pk, user=request.user)  
    if request.method == 'POST':
        query.delete()
        return redirect('curso:category_list')
    return render(request, 'curso/category_confirm_delete.html', {'object': query})


@login_required
def product_list(request: HttpResponse) -> HttpResponse:
    search_query = request.GET.get('search')
    queryset = Product.objects.filter(user=request.user)
    if search_query:
        queryset = queryset.filter(name__icontains=search_query)
    context = {"object_list": queryset, 'search_query': search_query}
    return render(request, "curso/product_list.html", context)

@login_required
def product_create(request):
    if request.method == "GET":
        form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("curso:product_list")
    return render(request, "curso/product_form.html", {"form": form})

@login_required
def product_update(request, pk: int):
    query = get_object_or_404(Product, id=pk, user=request.user)
    if request.method == "GET":
        form = ProductForm(instance=query)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("curso:product_list")
    return render(request, "curso/product_form.html", {"form": form})

@login_required
def product_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = get_object_or_404(Product, id=pk, user=request.user)
    return render(request, 'curso/product_detail.html', {'object': query})

@login_required
def product_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = get_object_or_404(Product, id=pk, user=request.user)
    if request.method == 'POST':
        query.delete()
        return redirect('curso:product_list')
    return render(request, 'curso/product_confirm_delete.html', {'object': query})

@login_required
def production_order_list(request):
    query = ProductionOrder.objects.all()
    context = {"object_list": query}
    return render(request, "curso/production_order_list.html", context)

@login_required
def production_order_create(request):
    if request.method == "GET":
        form = ProductionOrderForm()
    if request.method == "POST":
        form = ProductionOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Asignar el usuario autenticado
            order.save()
            return redirect("curso:production_order_list")
    return render(request, "curso/production_order_form.html", {"form": form})

@login_required
def production_order_update(request, pk: int):
    query = get_object_or_404(ProductionOrder, id=pk, user=request.user)
    if request.method == "GET":
        form = ProductionOrderForm(instance=query)
    if request.method == "POST":
        form = ProductionOrderForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("curso:production_order_list")
    return render(request, "curso/production_order_form.html", {"form": form})

@login_required
def production_order_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = get_object_or_404(ProductionOrder, id=pk, user=request.user)
    return render(request, 'curso/production_order_detail.html', {'object': query})

@login_required
def production_order_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = get_object_or_404(ProductionOrder, id=pk, user=request.user)
    if request.method == 'POST':
        query.delete()
        return redirect('curso:production_order_list')
    return render(request, 'curso/producttion_order_confirm_delete.html', {'object': query})

@login_required
def inventory_list(request):
    query = Inventory.objects.filter(user=request.user)
    context = {"object_list": query}
    return render(request, "curso/inventory_list.html", context)

@login_required
def inventory_create(request):
    if request.method == "GET":
        form = InventoryForm()
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.user = request.user  # Asignar el usuario autenticado
            inventory.save()
            return redirect("curso:inventory_list")
    return render(request, "curso/inventory_form.html", {"form": form})

@login_required
def inventory_update(request, pk: int):
    query = get_object_or_404(Inventory, id=pk, user=request.user)
    if request.method == "GET":
        form = InventoryForm(instance=query)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("curso:inventory_list")
    return render(request, "curso/inventory_form.html", {"form": form})

@login_required
def inventory_detail(request: HttpRequest, pk: int) -> HttpResponse:
    query = get_object_or_404(Inventory, id=pk, user=request.user)
    return render(request, 'curso/inventory_detail.html', {'object': query})

@login_required
def inventory_delete(request: HttpRequest, pk: int) -> HttpResponse:
    query = get_object_or_404(Inventory, id=pk, user=request.user)
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