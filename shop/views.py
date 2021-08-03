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
    return render(request, 'customerProducts.html', {})