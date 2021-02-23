from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = {
            'description', 'title', 'image',
        }
        widgets = {
            'description': forms.TextInput,
        }