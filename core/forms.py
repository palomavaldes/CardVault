from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-3 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-3 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') 

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-3 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-3 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-3 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Confirm your password',
        'class': 'w-full py-3 px-6 rounded-xl'
    }))