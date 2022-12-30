from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Імя користувача',
                               widget=forms.TextInput(attrs={'class': 'label-inp'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'label-inp'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'label-inp'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
