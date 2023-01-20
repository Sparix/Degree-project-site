from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout

from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView


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
        context = super().get_context_data(**kwargs)
        return context


class AboutProduct(DetailView):
    model = Product
    template_name = "forproducts.html"
    slug_url_kwarg = "product_slug"
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
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
        return reverse_lazy('stuff_form')


acc_name = [
    {'url_name': 'home', 'content': "Мої замовлення"},
    {'url_name': 'home', 'content': "Список бажань"},
    {'url_name': 'home', 'content': "Переглянуті товари"},
    {'url_name': 'stuff_form', 'content': "Добавить товар"},
]


class AddProduct(CreateView):
    form_class = AddProductForm
    template_name = 'staff_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_menu = acc_name.copy()
        if not self.request.user.is_staff:
            user_menu.pop(4)
        context['menu'] = user_menu
        context['active'] = 'person'
        return context


def profile(request):
    return render(request, 'cabinet.html', {'menu': acc_name})


def logout_user(request):
    logout(request)
    return redirect('home')
