from django.shortcuts import render
from apps.ecommerce.models import Product
from django.contrib.auth.decorators import login_required






@login_required
def home(request):
    products = Product.objects.all()   # 🔥 MUST
    return render(request, 'ecommerce/home.html', {
        'products': products
    })

def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})

