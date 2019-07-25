from .models import PurchaseOrder, Client, Vendor, CustomUser, Process
from bootstrap_modal_forms.forms import BSModalForm
from django import forms

class PurchaseOrderForm(BSModalForm):

    class Meta:
        model = PurchaseOrder
        fields = ('purchase_order_amount','purchase_order_amount_due')

class ProcessForm(BSModalForm):

    class Meta:
        model = Process
        fields = ('process_amount','process_amount_due')

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
