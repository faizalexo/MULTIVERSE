from django.shortcuts import render
from apps.ecommerce.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})
