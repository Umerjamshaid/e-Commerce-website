from django.db import models
import datetime

from django.conf.urls.static import static

# Create your models here.

# category of products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
# product of category
class Customer(models.Model):

    name = models.CharField(max_length=12)
    email = models.EmailField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=10)


    def __str__(self):
        return f'{self.name} {self.email} {self.phone} {self.address} {self.country}'

# product of category
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10) 
    description = models.TextField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    #adding sales model
    is_sales = models.BooleanField(default=False)
    sales_price = models.DecimalField(default=0, decimal_places=2, max_digits=6) 

    def __str__(self):
        return f'{self.name} {self.category} {self.price} {self.description} {self.image}'

# order of product
class Order(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE )
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    status = models.BooleanField(max_length=50, default='pending')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.Product} {self.Customer} {self.quantity} {self.address} {self.phone} {self.date} {self.status} {self.available}'
    