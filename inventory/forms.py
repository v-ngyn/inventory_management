from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import InventoryItem, Category

# sign up form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# add inventory form
class InventoryItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset = Category.objects.all(), initial = 0)
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'category']