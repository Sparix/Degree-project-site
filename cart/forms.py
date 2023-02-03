from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, initial=1,
                                      widget=forms.NumberInput(
                                          attrs={'class': 'let-s', 'min': '1', 'max': '20'}))
    update = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput())
