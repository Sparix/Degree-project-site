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
        model = Motherboard
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Название товара'}),
            'slug': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'URL адресса'}),
            'cost': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Цена товара'}),
            'manufactured': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Виробник'}),
            'photo': forms.FileInput(attrs={'class': 'image-form'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'published-form'}),
            'cat': forms.Select(attrs={'class': 'choice-select'}),
            'form_factor': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Форм-фактор'}),
            'sockets': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Сокет'}),
            'chipsets': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Чіпсет'}),
            'platforms': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Платформа'}),
            'memory_type': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Тип памяті'}),
            'power_phase': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Кільскість фаз живлення'}),
            'max_volume': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Максимальний обсяг'}),
            'slots': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Кількість слотів'}),
            'frequency': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Частота'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = False


class ProductAbout(forms.ModelForm):
    class Meta:
        model = Motherboard
        fields = '__all__'


'''class AddProductFormVideo(forms.ModelForm):
    class Meta:
        model = Videocard
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Название товара'}),
            'slug': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'URL адресса'}),
            'cost': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Цена товара'}),
            'manufactured': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Виробник'}),
            'photo': forms.FileInput(attrs={'class': 'image-form'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'published-form'}),
            'cat': forms.Select(attrs={'class': 'choice-select'}),
            'model_card': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Модель відеокарти'}),
            'power': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Живлення'}),
            'memory': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Обсяг памяті'}),
            'type_memory': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': "Тип пам'яті"}),
            'memory_frequency': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': "Частота пам'яті"}),
            'core_gpu': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Частота ядра GPU'}),
            'mini_power': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Необхідна потужність БЖ'}),
            'version_DirectX': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Версія DirectX'}),
            'type_cooling': forms.TextInput(attrs={'class': 'label-inp', 'placeholder': 'Тип охолодження'}),
        }

class ProductAboutVideo(forms.ModelForm):
    class Meta:
        model = Videocard
        fields = '__all__'''