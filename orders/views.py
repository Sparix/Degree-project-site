from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                form.instance.author = request.user
            else:
                form.instance.author = 'Anonymous_user'
            order = form.save()
            for item in cart:
                OrderItem.objects.create(orders=order,
                                         product=item['product'],
                                         cost=item['cost'],
                                         quantity=item['quantity'],
                                         )
            # очистка корзины
            cart.clear()
            return render(request, 'orders_valid.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders_create.html',
                  {'cart': cart, 'form': form})
