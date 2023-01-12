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
    model = Motherboard
    template_name = 'product.html'
    context_object_name = 'product'
    allow_empty = False

    def get_queryset(self):
        return Motherboard.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutProduct(CreateView, DetailView):
    form_class = ProductAbout
    model = Motherboard
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
        return reverse_lazy('profile')


class AddProduct(CreateView):
    form_class = AddProductForm
    template_name = 'staff_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def logout_user(request):
    logout(request)
    return redirect('home')

