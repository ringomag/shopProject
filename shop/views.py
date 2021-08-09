from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html', {"products":products, "categories":categories})

def categoryList(request, pk):
    category = Category.objects.get(id=pk)
    categoryChild = category.subcategory_set.all()
    print("ovo je categoryChild ", categoryChild)   
    return render(request, 'categories.html', {"category":category, "categoryChild":categoryChild})

def subcategoryList(request, pk, sk):
    category = Category.objects.get(id=pk)
    subcategory = Subcategory.objects.get(id=sk)
    subcategoryChild = subcategory.product_set.all()
    print(subcategory)
    print("ovo je subcategorychild, ", subcategoryChild)
    return render(request, 'subcategories.html', {"category":category, "subcategory":subcategory, "subcategoryChild":subcategoryChild})

def customerProducts(request):
    customers = Customer.objects.all()
    return render(request, 'customerProducts.html', {"customers":customers})

def order_details(request, pk):
    customers = Customer.objects.get(id=pk)
    orders = customers.order_set.all()
    orders_count = orders.count()
    return render(request, 'orderDetails.html', {"customers":customers, "orders":orders, "orders_count":orders_count})