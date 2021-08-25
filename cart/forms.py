from django import forms

PRODUCT_CHOICES_COUNT = [(i, str(i)) for i in range(10)]


class CartAddProductForm(forms.Form):
    count = forms.TypedChoiceField(choices=PRODUCT_CHOICES_COUNT, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
