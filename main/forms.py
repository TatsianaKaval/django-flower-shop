from django import forms
from .models import Order
from django.core.exceptions import ValidationError
import re


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'street', 'house', 'apartment', 'inscription']


    def clean_name(self):
        name_data = self.cleaned_data['name']

        if len(name_data) < 2:
            raise ValidationError("Name must be at least 2 symbols long.")
        
        return name_data
    
    def clean_phone(self):
        phone_data = self.cleaned_data['phone']

        if not re.match(r'^\+\d+$', phone_data):
            raise ValidationError("Phone number must start with a '+' and contain only digits.")
        if len(phone_data) != 13:
            raise ValidationError("Phone  must contain 13 symbols.")
        
        return phone_data
        
    def clean_street(self):
        street_data = self.cleaned_data['street']

        if not re.match(r'^[a-zA-Z.\-\d\s]+$', street_data):
            raise ValidationError("Street must contain only letters, '.', '-', digits(0-9) and spaces.")
        
        return street_data