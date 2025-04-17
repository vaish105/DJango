from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    model = Product
    class Meta:
        model=Product
        fields = '_all_'