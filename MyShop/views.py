from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import logout

from cart.forms import CartAddProductForm
from cart.cart import Cart
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class CategoriesHome(ListView):
    model = Categories
    template_name = 'main.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Categories.objects.all()


class ProductHome(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        product = Product.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
        slug = self.kwargs['cat_slug']
        manufactured = [manuf.manufactured for manuf in product]
        context = super().get_context_data(**kwargs)
        context['manufactured'] = sorted(set(manufactured))
        context['slug'] = slug
        context['price_from'] = 0
        context['price_to'] = 256000
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('cabinet')


class AddProduct(CreateView):
    form_class = AddProductForm
    template_name = 'staff_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def logout_user(request):
    logout(request)
    return redirect('home')


class PasswordChange(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('cabinet')
    template_name = "change_psw.html"


class ProfilePage(DetailView):
    model = UserProfile
    template_name = 'cabinet.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)


@login_required
def update_user(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return HttpResponse("invalid user_profile!")

    if request.method == "POST":
        update_user_form = UserForm2(data=request.POST, instance=request.user)
        update_profile_form = UserProfileForm(data=request.POST, instance=user_profile)

        if update_user_form.is_valid() and update_profile_form.is_valid():
            user = update_user_form.save()
            profile = update_profile_form.save(commit=False)
            profile.user = user

            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']

            profile.save()
            return redirect('cabinet')
        else:
            print(update_user_form.errors, update_profile_form.errors)
    else:
        update_user_form = UserForm2(instance=request.user)
        update_profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html',
                  {'update_user_form': update_user_form, 'update_profile_form': update_profile_form})


def product_detail(request, product_slug):
    product = get_object_or_404(Product,
                                slug=product_slug,
                                is_published=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'forproducts.html', {'product': product,
                                                'cart_product_form': cart_product_form})


class Search(ListView):
    """Поиск товаров"""
    model = Product
    template_name = 'search.html'
    context_object_name = 'product'
    allow_empty = False

    def get_queryset(self):
        search = Product.objects.filter(name__icontains=self.request.GET.get("search-prod"))

        if len(search) == 0:
            return ' '
        else:
            return search

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search_prod"] = self.request.GET.get("search-prod")
        return context


class FilterProduct(ListView):
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
        context['manufactured'] = sorted(set(manufactured))
        return context
