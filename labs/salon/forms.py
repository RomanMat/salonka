from django import forms
from .models import *

class AddMaster(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['name', 'serve']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form__input'}),
            'serve': forms.TextInput(attrs={'placeholder': 'Service', 'class': 'form__input'})
        }

class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form__input'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price', 'class': 'form__input'})
        }

class AddService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form__input'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description', 'class': 'form__input'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price', 'class': 'form__input'})
        }


class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password']
        widgets = {
            'login': forms.TextInput(attrs={'placeholder': 'Login', 'class': 'form__input'}),
            'password': forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form__input', 'type':'password'})
        }