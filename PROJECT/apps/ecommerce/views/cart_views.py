from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from apps.ecommerce.models import Cart, Product

from django.contrib.auth.decorators import login_required

@login_required
def cart(request):
    return render(request, 'ecommerce/cart.html')

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/shop/cart/')

from django.shortcuts import render

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)

    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'ecommerce/cart.html', {
        'cart_items': cart_items,
        'total': total
    })
from django.shortcuts import get_object_or_404

@login_required
def remove_from_cart(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user=request.user)
    item.delete()
    return redirect('/shop/cart/')


def cart(request):
    return render(request, 'ecommerce/cart.html')