from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import CartItem

@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items})


