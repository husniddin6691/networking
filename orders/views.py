from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

def create_order(request):
    return render(request, 'orders/order_created.html')
