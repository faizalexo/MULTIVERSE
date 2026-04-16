from django.shortcuts import render
from apps.ecommerce.models import Product
from django.contrib.auth.decorators import login_required






@login_required
def home(request):
    return render(request, 'ecommerce/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})
