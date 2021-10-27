from django import forms
from django.db.models import fields
from Product.models import Product


class ProductForm(forms.ModelForm):
    '''
        Form for Product model
    '''

    class Meta:
        model = Product
        fields = '__all__'


