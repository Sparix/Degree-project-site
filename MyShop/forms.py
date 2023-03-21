from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Імя користувача',
                               widget=forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Імя користувача'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'label-inp', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'label-inp', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Імя користувача',
                               widget=forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Імя користувача'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'label-inp', 'placeholder': 'Пароль'}))


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'cost', 'is_published', 'photo', 'manufactured', 'cat', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Название товара'}),
            'cost': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Цена товара'}),
            'photo': forms.FileInput(attrs={'class': 'image-form'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'published-form'}),
            'manufactured': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Виробник товара'}),
            'cat': forms.Select(attrs={'class': 'choice-select'}),
            'content': forms.Textarea(attrs={'class': 'text-area'}),
        }


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'label-inp', 'placeholder': 'Введіть старий пароль'}))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'label-inp', 'placeholder': 'Введіть новий пароль'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'label-inp', 'placeholder': 'Повторіть новий пароль'}))

    class Meta:
        model = User
        fields = {
            'old_password', 'new_password1', 'new_password2'
        }


class UserForm2(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Введіть новий username'}),
            'last_name': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Введіть фаміляю'}),
            'first_name': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': "Введіть Ім'я"}),
            'email': forms.EmailInput(attrs={'class': 'label-inp', 'placeholder': 'Введіть Email'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar',)

        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'image-form'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'name', 'advantages', 'disadvantages')

        widgets = {
            'comment': forms.Textarea(attrs={'class': 'area-comment', 'placeholder': 'Ваш відгук'}),
            'name': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': "Ваше ім'я "}),
            'advantages': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': "Переваги"}),
            'disadvantages': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': "Недоліки"}),
        }