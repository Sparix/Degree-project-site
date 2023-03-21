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

    def total_rating(self, product_slug, **kwargs):
        review = Comment.objects.filter(product__slug=product_slug)
        rating = sum([rat.rating for rat in review])
        if rating > 0:
            rating /= len(review)

        context = kwargs
        context['rating'] = round(rating, 1)
        return context
