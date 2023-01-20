from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
        fields = ('name', 'cost', 'manufactured', 'is_published', 'photo', 'cat', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Название товара'}),
            'cost': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Цена товара'}),
            'manufactured': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Виробник'}),
            'photo': forms.FileInput(attrs={'class': 'image-form'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'published-form'}),
            'cat': forms.Select(attrs={'class': 'choice-select'}),
            'content': forms.Textarea(attrs={'class': 'text-area'}),
        }
