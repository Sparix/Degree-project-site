from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import logout

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
        return reverse_lazy('cabinet')


class AddProduct(CreateView):
    form_class = AddProductForm
    template_name = 'staff_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


'''def profile(request):
    return render(request, 'cabinet.html', )'''


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
