from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cart = Cart(self.request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
        context['cart'] = cart
        return context
