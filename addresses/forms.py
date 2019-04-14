from django import forms

from .models import Addresses

class AddressForm(forms.ModelForm):
    class Meta:
        model = Addresses
        # fields = '__all__'
        exclude = ['billing_profile', 'address_type']
