from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone_number', 'city',]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'order-input', 'placeholder': "Ім'я"}),
            'last_name': forms.TextInput(attrs={'class': 'order-input', 'placeholder': "Прізвище"}),
            'email': forms.EmailInput(attrs={'class': 'order-input', 'placeholder': "Email"}),
            'address': forms.TextInput(attrs={'class': 'order-input', 'placeholder': "Адреса доставки"}),
            'city': forms.TextInput(attrs={'class': 'order-input', 'placeholder': "Місто"}),
            'phone_number': forms.TextInput(attrs={'class': 'order-input', 'placeholder': "Номер телефона"})
        }
