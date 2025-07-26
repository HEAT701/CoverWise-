
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Warranty

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class WarrantyForm(forms.ModelForm):
    class Meta:
        model = Warranty
        fields = ['product_name', 'product_id', 'expiry_date', 'qr_data', 'warranty_image']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'warranty_image': forms.ClearableFileInput(attrs={'multiple': False}),
        }