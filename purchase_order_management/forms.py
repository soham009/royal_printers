from .models import PurchaseOrder
from bootstrap_modal_forms.forms import BSModalForm
from django import forms

class PurchaseOrderForm(BSModalForm):
    class Meta:
        model = PurchaseOrder

class PurchaseForm(forms.Form):
    pass