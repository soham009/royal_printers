from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import PurchaseOrder
from bootstrap_modal_forms.generic import BSModalDeleteView
from django.urls import reverse_lazy

class PurchaseOrderDeleteView(BSModalDeleteView):
    model = PurchaseOrder
    template_name = 'purchase_order_management/purchase_order_list_delete.html'
    success_message = 'Success: Purchase order was deleted.'
    success_url = reverse_lazy('purchase_order_management:purchase_order_list')

# Create your views here.
def purchase_form(request):
    data = { }
    return render(request, 'purchase_order.html', data )

def purchase_list(request):
    """
    Generates the list of all the purchase orders and the processes in each of the purchase order.
    Parameters: HttpRequest object
    Returns : Nothing
    """
    # Get all the purchase orders or raise a 404 exception if no purchase orders
    purchase_orders = PurchaseOrder.objects.all()

    # Generate the list of processes for each purchase order
    process_list = []
    for purchase_order in purchase_orders:
        # Getting all the processes in a purchase order using manytomany_relation.all() method
        # and appending it to the above process_list.
        process_list.append(purchase_order.purchase_order_process_relation.all())

    data = {
        'purchase_orders': zip(purchase_orders,process_list)
     }
    return render(request, 'purchase_order_management/purchase_order_list.html', data )

def home(request):
    data = { }
    return render(request, 'home.html', data )

