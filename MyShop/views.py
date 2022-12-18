from django.shortcuts import render, HttpResponse
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
    template_name = "test.html"
    slug_url_kwarg = "product_slug"
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def test(request):
    return render(request, 'register.html')
