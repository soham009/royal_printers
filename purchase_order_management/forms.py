from .models import PurchaseOrder, Client, Vendor, CustomUser
from bootstrap_modal_forms.forms import BSModalForm
from django import forms

class PurchaseForm(forms.Form):
    pass

class ClientForm(BSModalForm):
    
    class Meta:
        model = Client
        exclude = ('pk',)

class VendorForm(BSModalForm):
    
    class Meta:
        model = Vendor
        exclude = ('pk',)

class CustomUserForm(BSModalForm):
    class Meta:
        model = CustomUser
        fields = ['user_role']