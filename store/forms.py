from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'last_name', 'city', 'address', 'phone']

        widgets = {
        'name': forms.TextInput(attrs={"class":"order-form"}),
        'last_name': forms.TextInput(attrs={"class":"order-form"}),
        'city': forms.TextInput(attrs={"class":"order-form"}),
        'address': forms.TextInput(attrs={"class": "order-form"}),
        'phone': forms.NumberInput(attrs={"class":"order-form"}),
        }