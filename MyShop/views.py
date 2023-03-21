from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views import View
from django.contrib import messages

from cart.forms import CartAddProductForm
from cart.cart import Cart
from orders.models import *
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .mixins import DataMixin


class CategoriesHome(DataMixin, ListView):
    model = Categories
    template_name = 'main.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Categories.objects.all()


class ProductHome(DataMixin, ListView):
    model = Product
    paginate_by = 8
    template_name = 'product.html'
    context_object_name = 'product'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        cart_product_form = CartAddProductForm()
        product_cart = Product.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
        slug = self.kwargs['cat_slug']
        manufactured = [manuf.manufactured for manuf in product_cart]
        context = super().get_context_data(**kwargs)
        context['manufactured'] = sorted(set(manufactured))
        context['slug'] = slug
        context['price_from'] = 0
        context['price_to'] = 256000
        context['cart_product_form'] = cart_product_form
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class AddProduct(DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'staff_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))


class PasswordChange(DataMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('cabinet')
    template_name = "change_psw.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


'''def update_user(request):
    print(*UserProfile.objects.all())
    try:
        user_profile = UserProfile.objects.get(user_id=request.user.id)
    except UserProfile.DoesNotExist:
        return HttpResponse("invalid user_profile!")

    if request.method == "POST":
        update_user_form = UserForm2(data=request.POST, instance=request.user)
        update_profile_form = UserProfileForm(data=request.POST, instance=user_profile)

        if update_user_form.is_valid() and update_profile_form.is_valid():
            user = update_user_form.save()
            profile = update_profile_form.save(commit=False)
            profile.user = user
            profile.avatar = request.FILES['avatar']

            profile.save()
            return redirect('cabinet')
        else:
            print(update_user_form.errors, update_profile_form.errors)
    else:
        update_user_form = UserForm2(instance=request.user)
        update_profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html',
                  {'update_user_form': update_user_form, 'update_profile_form': update_profile_form})'''


@login_required
def update_user(request):
    if request.method == 'POST':
        update_user_form = UserForm2(request.POST, request.FILES, instance=request.user)
        update_profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if update_user_form.is_valid() and update_profile_form.is_valid():
            user = update_user_form.save(commit=False)

            user.save()
            profile = update_profile_form.save(commit=False)
            profile.user = user

            profile.save()
            return redirect('cabinet')
        else:
            print(update_user_form.errors, update_profile_form.errors)
    else:
        update_profile_form = UserProfileForm(instance=request.user.userprofile)
        update_user_form = UserForm2(instance=request.user)
    context = {'update_user_form': update_user_form,  # basic user form
               'update_profile_form': update_profile_form  # user profile form
               }
    return render(request, 'edit_profile.html', context)


class ProfilePage(DataMixin, DetailView):
    model = UserProfile
    template_name = 'cabinet.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


def product_detail(request, product_slug):
    product = get_object_or_404(Product,
                                slug=product_slug,
                                is_published=True)
    review = Comment.objects.filter(product__slug=product_slug)
    rating = sum([rat.rating for rat in review])
    if rating > 0:
        rating /= len(review)

    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'forproducts.html', {'product': product,
                                                'cart_product_form': cart_product_form, 'cart': cart,
                                                'rating': round(rating, 1)})


class Search(DataMixin, ListView):
    """Поиск товаров"""
    model = Product
    paginate_by = 10
    template_name = 'search.html'
    context_object_name = 'product'
    allow_empty = False

    def get_queryset(self):
        search = Product.objects.filter(Q(name__icontains=self.request.GET.get("search-prod")) | Q(
            content__icontains=self.request.GET.get("search-prod")))

        if len(search) == 0:
            return ' '
        else:
            return search

    def get_context_data(self, *args, **kwargs):
        cart_product_form = CartAddProductForm()
        context = super().get_context_data(*args, **kwargs)
        context['cart_product_form'] = cart_product_form
        context["search_prod"] = self.request.GET.get("search-prod")
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class FilterProduct(DataMixin, ListView):
    paginate_by = 8
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    allow_empty = False

    def get_queryset(self):
        price_from = self.request.GET.get('price_from', 0)
        price_to = self.request.GET.get('price_to', 256000)
        ordering = self.request.GET.get('ordering', '-cost')
        manufactured = [manuf.manufactured for manuf in
                        Product.objects.filter(is_published=True, cat__slug=self.kwargs['cat_slug'])]
        brand = self.request.GET.getlist('brand', manufactured)
        prod = Product.objects.filter(is_published=True, cat__slug=self.kwargs['cat_slug'],
                                      manufactured__in=brand).filter(
            cost__gte=price_from).filter(cost__lte=price_to).order_by(ordering)
        if len(prod) == 0:
            return ' '
        else:
            return prod

    def get_context_data(self, *, object_list=None, **kwargs):
        cart_product_form = CartAddProductForm()
        slug = self.kwargs['cat_slug']
        price_from = self.request.GET.get('price_from', 0)
        price_to = self.request.GET.get('price_to', 256000)
        product = Product.objects.filter(is_published=True, cat__slug=self.kwargs['cat_slug'])
        brands = [manuf.manufactured for manuf in product]
        brand = set(self.request.GET.getlist('brand', brands))
        manufactured = [manuf.manufactured for manuf in product]
        context = super().get_context_data(**kwargs)
        context['price_from'] = price_from
        context['price_to'] = price_to
        context['slug'] = slug
        context['brand'] = brand
        context['cart_product_form'] = cart_product_form
        context['manufactured'] = sorted(set(manufactured))
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class UserOrder(DataMixin, ListView):
    model = Order
    template_name = 'Orders_user.html'
    context_object_name = 'orders'

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Order.objects.filter(author=self.request.user)
        else:
            return Order.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_item'] = OrderItem.objects.filter()
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


def comments(request, product_slug):
    product = Product.objects.get(slug=product_slug,
                                  is_published=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data_form = form.save(commit=False)
            data_form.rating = request.POST['rate']
            data_form.author = request.user
            data_form.product = product
            data_form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        cart_prod_form = CartAddProductForm()
        form_comment = CommentForm
        comment = Comment.objects.filter(product__slug=product.slug)
        return render(request, 'comments.html',
                      {'product': product, "cart_prod_form": cart_prod_form, "form_comment": form_comment,
                       'comment': comment})
