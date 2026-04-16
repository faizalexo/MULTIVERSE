from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.ecommerce.models import Cart, Product


# 🛒 VIEW CART (sidebar + page both support)
@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)

    total = sum(item.product.price * item.quantity for item in cart_items)

    # 🔥 AJAX detect (sidebar load)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'ecommerce/cart.html', {
            'cart_items': cart_items,
            'total': total
        })

    # normal page load
    return render(request, 'ecommerce/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


# ➕ ADD TO CART
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


# ❌ REMOVE ITEM
@login_required
def remove_from_cart(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user=request.user)
    item.delete()

    return redirect('cart')


# 🔼 INCREASE
@login_required
def increase_quantity(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user=request.user)
    item.quantity += 1
    item.save()

    return redirect('cart')


# 🔽 DECREASE
@login_required
def decrease_quantity(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')

    from django.http import JsonResponse

@login_required
def update_cart(request, cart_id, action):
    item = get_object_or_404(Cart, id=cart_id, user=request.user)

    if action == 'increase':
        item.quantity += 1

    elif action == 'decrease':
        if item.quantity > 1:
            item.quantity -= 1
        else:
            item.delete()
            return JsonResponse({'deleted': True})

    item.save()

    return JsonResponse({
        'quantity': item.quantity,
        'price': item.product.price * item.quantity
    })