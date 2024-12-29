from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField()  
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    production_time = models.IntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

class ProductionOrder(models.Model):
    order_number = models.CharField(max_length=50)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    status = models.CharField(max_length=50)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return self.order_number
   

class Inventory(models.Model):
    order_number = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    location = models.CharField(max_length=100)  
    stock_quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.product.name} - {self.location}"
