from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction # Import transaction for atomicity
from django.contrib import messages # Good for user feedback
from item.models import Item
from .models import Cart, CartItem
from django.views.decorators.http import require_POST
from django.http import JsonResponse



# Assuming your Order models and form are in an 'order' app
# Adjust these imports based on where your Order models and form actually reside
from orders.models import Order, OrderItem
from orders.forms import OrderCreateForm

@require_POST

@require_POST
def cart_add(request, item_pk):
    cart_id = request.session.get('cart_id')
    
    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    
    item = get_object_or_404(Item, pk=item_pk)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    
    if not created:
        cart_item.quantity = 1
    
    cart_item.save()
    
    response_data = {
        "success":True,
        "message": f'Added {item.name} to cart'
    }

    return JsonResponse(response_data)
    
    
def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart=None
    
    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
    if not cart or not cart.items.exists():
        cart=None
    
    return render(request, "cart/detail.html", {"cart":cart})
    
def cart_remove(request, item_pk):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart, id=cart_id)
    item = get_object_or_404(CartItem, pk=item_pk, cart=cart)
    item.delete()
    
    return redirect("cart:cart_detail")
