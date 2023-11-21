from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'catalog/product.html', {'product': product})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/list.html', {'products': products})

