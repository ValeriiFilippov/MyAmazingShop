from django.views.decorators.http import require_POST
from cart.cart import Cart
from django.shortcuts import get_object_or_404, render, redirect
from shop.models import Product
from .forms import CartAddProductForm
from django.conf import settings


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        c_data = form.cleaned_data
        cart.add(product=product,
                 count=c_data['count'],
                 update_count=c_data['update'])

    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', context={settings.SESSION_ID_CART: cart})
