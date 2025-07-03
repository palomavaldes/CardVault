from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "email", "address", "city", "state", "postal_code"]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full py-3 px-6 rounded-xl',
                'placeholder': 'Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full py-3 px-6 rounded-xl',
                'placeholder': 'Email'
            }),
            'address': forms.TextInput(attrs={
                'class': 'w-full py-3 px-6 rounded-xl',
                'placeholder': 'Address'
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full py-3 px-6 rounded-xl',
                'placeholder': 'City'
            }),
            'state': forms.TextInput(attrs={
                'class': 'w-full py-3 px-6 rounded-xl',
                'placeholder': 'State'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'w-full py-3 px-6 rounded-xl',
                'placeholder': 'Postal Code'
            }),
        }