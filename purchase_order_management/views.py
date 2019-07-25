from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from .models import PurchaseOrder, Client, Vendor, CustomUser, Paper
from bootstrap_modal_forms.generic import BSModalDeleteView, BSModalUpdateView
from django.urls import reverse_lazy, reverse
from .forms import ClientForm, VendorForm, CustomUserForm, PurchaseOrderForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
import datetime


# Create your views here.

class CustomUserUpdateView(BSModalUpdateView):
    model = CustomUser
    template_name = 'purchase_order_management/user_list_update.html'
    form_class = CustomUserForm
    success_message = 'Success: User was updated.'
    success_url = reverse_lazy('purchase_order_management:user_list')

class PurchaseOrderDeleteView(BSModalDeleteView):
    model = PurchaseOrder
    template_name = 'purchase_order_management/purchase_order_list_delete.html'
    success_message = 'Success: Purchase order was deleted.'
    success_url = reverse_lazy('purchase_order_management:purchase_order_list')

class PurchaseOrderUpdateView(BSModalUpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'purchase_order_management/purchase_order_list_update.html'
    success_message = 'Success: Purchase Order was updated.'
    success_url = reverse_lazy('purchase_order_management:purchase_order_list')

class VendorUpdateView(BSModalUpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'purchase_order_management/vendor_list_update.html'
    success_message = 'Success: Vendor was updated.'
    success_url = reverse_lazy('purchase_order_management:vendor_list')

def purchase_list(request):
    """Generates the list of all the purchase orders and the processes in each of the purchase order.
    Parameters: HttpRequest object
    Returns : Nothing"""

    user_role = request.user.user_role

    # Get all the purchase orders or raise a 404 exception if no purchase orders
    purchase_orders = PurchaseOrder.objects.all()

    # Generate the list of processes for each purchase order
    process_list = []
    for purchase_order in purchase_orders:
        # Getting all the processes in a purchase order using manytomany_relation.all() method
        # and appending it to the above process_list.
        process_list.append(purchase_order.purchase_order_process_relation.all())

    data = {
        'purchase_orders': zip(purchase_orders,process_list),
        'user_role': user_role
        
     }
    return render(request, 'purchase_order_management/purchase_order_list.html', data )

def client_list(request):
    """Generates the list of all the clients.
    Parameters: HttpRequest object
    Returns : Nothing"""
    user_role = request.user.user_role
    # Get all the clients.
    clients = Client.objects.all()
    clients_total_amount = {}
    clients_total_amount_due = {}
    for client in clients:
        total_amount = 0
        total_amount_due = 0
        for purchase_order in client.purchaseorder_set.all():
            total_amount += purchase_order.purchase_order_amount
            total_amount_due += purchase_order.purchase_order_amount_due
        clients_total_amount[client.pk]=total_amount
        clients_total_amount_due[client.pk]=total_amount_due

    data = {
        'clients': clients,
        'clients_total_amount': clients_total_amount,
        'clients_total_amount_due': clients_total_amount_due,
        'user_role': user_role
     }
    return render(request, 'purchase_order_management/client_list.html', data )

def vendor_list(request):
    """Generates the list of all the vendors.
    Parameters: HttpRequest object
    Returns : Nothing"""
    user_role = request.user.user_role
    # Get all the clients.
    vendors = Vendor.objects.all()
    data = {
        'vendors': vendors,
        'user_role': user_role
     }
    return render(request, 'purchase_order_management/vendor_list.html', data )

def home(request):
    data = { }
    return render(request, 'home.html', data )

def purchase_order_form(request):
    user_role = request.user.user_role
    vendors = Vendor.objects.all()
    clients = Client.objects.all()

    data = {
        'user_role': user_role,
        'vendors': vendors,
        'clients': clients
    }
    return render(request, 'purchase_order_management/purchase_order_form.html', data )


def user_sign_in(request):
    """Logs in a user if the credentials are valid and the user is active, 
    else redirects to the same page and displays an error message."""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('purchase_order_management:purchase_order_form'))   
        else:
            return render(request, 'purchase_order_management/registration/sign_in.html',{'error_message': 'Username or Password Incorrect!'})

    else:
        return render(request, 'purchase_order_management/registration/sign_in.html')

@login_required
def user_sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('purchase_order_management:sign_in')) 


def user_sign_up(request):
    """Registers a user"""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'purchase_order_management/registration/sign_up.html',{'error_message':'Passwords do not match!'})
        if CustomUser.objects.filter(username = username).exists():
            return render(request, 'purchase_order_management/registration/sign_up.html',{'error_message':'Username already exists!'})
        else:
            # Role 2 is for admin, 1 is for super admin.
            user = CustomUser.objects.create(username=username, password= make_password(password), user_role=2)
            login(request, user)
            return HttpResponseRedirect(reverse('purchase_order_management:purchase_order_form'))
    else:
        return render(request, 'purchase_order_management/registration/sign_up.html')

def error_404(request):
    data = { }
    return render(request, 'purchase_order_management/404.html', data )

def profile(request):
    """Generates User Profile Details
    Parameters: HttpRequest object
    Returns : Nothing"""
    username = request.user.username
    user_role = request.user.user_role
    login = request.user.last_login + datetime.timedelta(hours=5,minutes=30)
    date_join = request.user.date_joined + datetime.timedelta(hours=5,minutes=30)
    data = { 'username': username , 'login' : login, 'date_join' : date_join, 'user_role':user_role }
    return render(request, 'purchase_order_management/profile.html', data )


def user_list(request):
    user_role = request.user.user_role
    users = CustomUser.objects.all()
    data = { 'users' : users, 'user_role': user_role }
    return render(request, 'purchase_order_management/user_list.html',data)

def report_error(request):
    """Form for taking User Errors
    Parameters: HttpRequest object
    Returns : Nothing"""
    user_role = request.user.user_role
    data = { 'user_role': user_role}
    return render(request, 'purchase_order_management/report_error.html', data )


def purchase_order_form_submit(request):
    """Creates a new purchase order
        Parameters: request object.
        Returns: Redirects to purchase order list if the purchase order is created successfully.
    """
    if request.method == "POST":
        # Get all data relating to purchase order.
        purchase_order_item = request.POST['purchase_order_item']
        purchase_order_item_quantity = request.POST['purchase_order_item_quantity']
        purchase_order_size = request.POST['purchase_order_size']
        purchase_order_number_of_columns = request.POST['purchase_order_number_of_columns']
        purchase_order_purchase_date = request.POST['purchase_order_purchase_date']
        purchase_order_purchase_by = request.POST['purchase_order_purchase_by']
        purchase_order_name = request.POST['purchase_order_name']
        purchase_order_po_number = request.POST['purchase_order_po_number']
        purchase_order_number = request.POST['purchase_order_number']
        purchase_order_amount = request.POST['purchase_order_amount']

        # Get the user object who creates the purchase order and the client object whose
        # purchase order it is.
        purchase_order_user_id = CustomUser.objects.get(pk=request.user.pk)
        purchase_order_client_id = Client.objects.get(pk=request.POST['purchase_order_client'])

        # Create the purchase order object.
        purchase_order = PurchaseOrder.objects.create(purchase_order_item = purchase_order_item,
                                                        purchase_order_item_quantity = purchase_order_item_quantity, 
                                                        purchase_order_size = purchase_order_size, 
                                                        purchase_order_number_of_columns = purchase_order_number_of_columns, 
                                                        purchase_order_purchase_date = purchase_order_purchase_date, 
                                                        purchase_order_purchase_by = purchase_order_purchase_by, 
                                                        purchase_order_name = purchase_order_name, 
                                                        purchase_order_po_number = purchase_order_po_number, 
                                                        purchase_order_number = purchase_order_number, 
                                                        purchase_order_amount = purchase_order_amount,
                                                        purchase_order_amount_due = purchase_order_amount,
                                                        purchase_order_user_id = purchase_order_user_id, 
                                                       purchase_order_client_id = purchase_order_client_id)
        # Check if paper process is present.
        if request.POST.get('paper_checkbox', False) == 'paper':
            # Get the paper process data.
            paper_quantity = request.POST['paper_quantity']
            paper_color = request.POST['paper_color']
            paper_gsm = request.POST['paper_gsm']
            paper_number_of_sheets = request.POST['paper_number_of_sheets']
            paper_rate = request.POST['paper_rate']
            
            process_name = 'Paper'
            process_size = request.POST['paper_size']

            # Calculate the process amount.
            process_amount = float(paper_rate)*int(paper_quantity)

            # Get the vendor to which the process is assigned.
            process_vendor_id = Vendor.objects.get(pk=request.POST['paper_vendor'])
            
            # Create the paper object.
            paper = Paper.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, paper_quantity = paper_quantity,
                                    paper_color = paper_color, paper_gsm = paper_gsm,
                                     paper_number_of_sheets = paper_number_of_sheets,
                                     paper_rate = paper_rate,process_vendor_id = process_vendor_id
                                     )

            # Add the paper object in the many to many relation with the above purchase order object.
            purchase_order.purchase_order_process_relation.add(paper)
    return HttpResponseRedirect(reverse('purchase_order_management:purchase_order_list'))

