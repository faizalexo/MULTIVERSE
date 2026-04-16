from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from apps.ecommerce.models import Cart, Product
from django.contrib import messages
from apps.ecommerce.models import Cart, Order, OrderItem




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
@require_POST
def add_to_cart(request, product_id):

    if request.method == "POST":

        product = get_object_or_404(Product, id=product_id)

        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        # 🛒 cart count
        cart_count = Cart.objects.filter(user=request.user).count()

        return JsonResponse({
            "success": True,
            "cart_count": cart_count
        })

    return JsonResponse({"success": False})


# ❌ REMOVE ITEM
@login_required
def remove_from_cart(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user=request.user)
    item.delete()

    return redirect('cart')








@login_required
def update_cart(request, cart_id, action):

    item = get_object_or_404(Cart, id=cart_id, user=request.user)

    if action == "increase":
        item.quantity += 1
        item.save()

    elif action == "decrease":
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
            return JsonResponse({"deleted": True})

    # 💰 calculations
    item_total = item.product.price * item.quantity
    cart_items = Cart.objects.filter(user=request.user)
    cart_total = sum(i.product.price * i.quantity for i in cart_items)

    return JsonResponse({
        "quantity": item.quantity,
        "item_total": item_total,
        "cart_total": cart_total,
        "deleted": False
    })


@login_required
def checkout(request):
    if request.method == "POST":
        cart_items = Cart.objects.filter(user=request.user)

        total = sum(item.product.price * item.quantity for item in cart_items)

        order = Order.objects.create(
            user=request.user,
            total_amount=total
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        cart_items.delete()

        return JsonResponse({'success': True})