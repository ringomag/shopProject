from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.

class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.firstName + self.lastName

class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    
    def __str__(self):
        return self.categoryName 

class Subcategory(models.Model):
    subcategoryName = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, on_delete=SET_NULL)

    def __str__(self):
        return self.subcategoryName

class Product(models.Model):
    productName = models.CharField(max_length=100)
    price = models.FloatField()
    subcategory = models.ForeignKey(Subcategory, null=True, on_delete=SET_NULL)

    def __str__(self):
        return self.productName

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

