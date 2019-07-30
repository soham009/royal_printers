from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from .models import PurchaseOrder, Client, Vendor, CustomUser, Paper, Process, Binding, CTP, SpecialProcess, RaiseUV, Varnish, Lamination, Positive, Printing, Punching, Pasting, Folding, Creasing, Punch, Block, FourCol
from bootstrap_modal_forms.generic import BSModalDeleteView, BSModalUpdateView, BSModalCreateView
from django.urls import reverse_lazy, reverse
from .forms import ClientForm, VendorForm, CustomUserForm, PurchaseOrderForm, ProcessForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
import datetime


# Create your views here.
@method_decorator(login_required, name='dispatch')
class CustomUserUpdateView(BSModalUpdateView):
    model = CustomUser
    template_name = 'purchase_order_management/user_list_update.html'
    form_class = CustomUserForm
    success_message = 'Success: User was updated.'
    success_url = reverse_lazy('purchase_order_management:user_list')

@method_decorator(login_required, name='dispatch')
class PurchaseOrderDeleteView(BSModalDeleteView):
    model = PurchaseOrder
    template_name = 'purchase_order_management/purchase_order_list_delete.html'
    success_message = 'Success: Purchase order was deleted.'
    success_url = reverse_lazy('purchase_order_management:purchase_order_list')

@method_decorator(login_required, name='dispatch')
class PurchaseOrderUpdateView(BSModalUpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'purchase_order_management/purchase_order_list_update.html'
    success_message = 'Success: Purchase Order was updated.'
    success_url = reverse_lazy('purchase_order_management:purchase_order_list')

@method_decorator(login_required, name='dispatch')
class ProcessDeleteView(BSModalDeleteView):
    model = Process
    template_name = 'purchase_order_management/process_list_delete.html'
    success_message = 'Success: Process was deleted.'
    success_url = reverse_lazy('purchase_order_management:process_list')

@method_decorator(login_required, name='dispatch')
class ProcessUpdateView(BSModalUpdateView):
    model = Process
    form_class = ProcessForm
    template_name = 'purchase_order_management/process_list_update.html'
    success_message = 'Success: Process was updated.'
    success_url = reverse_lazy('purchase_order_management:process_list')


@method_decorator(login_required, name='dispatch')
class PurchaseOrderProcessDetailDeleteView(BSModalDeleteView):
    model = Process
    template_name = 'purchase_order_management/process_list_delete.html'
    success_message = 'Success: Process was deleted.'

    def get_success_url(self,**kwargs):
        process = Process.objects.get(pk=self.kwargs['pk'])
        purchase_order_id = process.process_purchase_order_id
        return reverse_lazy('purchase_order_management:purchase_order_list_detail', kwargs={'pk': purchase_order_id })


@method_decorator(login_required, name='dispatch')
class PurchaseOrderProcessDetailUpdateView(BSModalUpdateView):
    model = Process
    form_class = ProcessForm
    template_name = 'purchase_order_management/process_list_update.html'
    success_message = 'Success: Process was updated.'

    def get_success_url(self,**kwargs):
        process = Process.objects.get(pk=self.kwargs['pk'])
        purchase_order_id = process.process_purchase_order_id
        return reverse_lazy('purchase_order_management:purchase_order_list_detail', kwargs={'pk': purchase_order_id })


@method_decorator(login_required, name='dispatch')
class ClientCreateView(BSModalCreateView):
    template_name = 'purchase_order_management/client_list_create.html'
    form_class = ClientForm
    success_message = 'Success: Client was created.'
    success_url = reverse_lazy('purchase_order_management:client_list')


@method_decorator(login_required, name='dispatch')
class VendorCreateView(BSModalCreateView):
    template_name = 'purchase_order_management/vendor_list_create.html'
    form_class = VendorForm
    success_message = 'Success: Vendor was created.'
    success_url = reverse_lazy('purchase_order_management:vendor_list')


@method_decorator(login_required, name='dispatch')
class VendorProcessDetailDeleteView(BSModalDeleteView):
    model = Process
    template_name = 'purchase_order_management/process_list_delete.html'
    success_message = 'Success: Process was deleted.'

    def get_success_url(self,**kwargs):
        process = Process.objects.get(pk=self.kwargs['pk'])
        vendor_id = process.process_vendor_id
        return reverse_lazy('purchase_order_management:vendor_list_detail', kwargs={'pk': vendor_id })

@method_decorator(login_required, name='dispatch')
class VendorProcessDetailUpdateView(BSModalUpdateView):
    model = Process
    form_class = ProcessForm
    template_name = 'purchase_order_management/process_list_update.html'
    success_message = 'Success: Process was updated.'

    def get_success_url(self,**kwargs):
        process = Process.objects.get(pk=self.kwargs['pk'])
        vendor_id = process.process_vendor_id
        return reverse_lazy('purchase_order_management:vendor_list_detail', kwargs={'pk': vendor_id })

@method_decorator(login_required, name='dispatch')
class ClientPurchaseOrderDetailDeleteView(BSModalDeleteView):
    model = PurchaseOrder
    template_name = 'purchase_order_management/purchase_order_list_delete.html'
    success_message = 'Success: Purchase order was deleted.'

    def get_success_url(self,**kwargs):
        purchase_order = PurchaseOrder.objects.get(pk=self.kwargs['pk'])
        client_id = purchase_order.purchase_order_client_id
        return reverse_lazy('purchase_order_management:client_list_detail', kwargs={'pk': client_id })

@method_decorator(login_required, name='dispatch')
class ClientPurchaseOrderDetailUpdateView(BSModalUpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'purchase_order_management/purchase_order_list_update.html'
    success_message = 'Success: Purchase Order was updated.'

    def get_success_url(self,**kwargs):
        purchase_order = PurchaseOrder.objects.get(pk=self.kwargs['pk'])
        client_id = purchase_order.purchase_order_client_id
        return reverse_lazy('purchase_order_management:client_list_detail', kwargs={'pk': client_id })

@login_required
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
        # Getting all the processes in a purchase order.
        # and appending it to the above process_list.
        process_list.append(purchase_order.process_set.all())

    data = {
        'purchase_orders': zip(purchase_orders,process_list),
        'user_role': user_role
     }
    return render(request, 'purchase_order_management/purchase_order_list.html', data )

@login_required
def purchase_order_list_details(request, pk):
    user_role = request.user.user_role
    purchase_order = PurchaseOrder.objects.get(pk=pk)
    processes = purchase_order.process_set.all()

    data = { 
        'processes':processes,
        'user_role': user_role
    }
    return render(request,'purchase_order_management/purchase_order_detail_view.html',data)


@login_required
def process_list(request):
    """Generates the list of all the processes.
    Parameters: HttpRequest object
    Returns : Nothing"""

    user_role = request.user.user_role

    # Get all the processes or raise a 404 exception if no purchase orders
    processes = Process.objects.all()

    data = {
        'processes': processes,
        'user_role': user_role
     }
    return render(request, 'purchase_order_management/process_list.html', data )

@login_required
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

@login_required
def client_list_details(request, pk):
    user_role = request.user.user_role
    client = Client.objects.get(pk=pk)
    purchase_orders = client.purchaseorder_set.all()

    process_list = []
    for purchase_order in purchase_orders:
        # Getting all the processes in a purchase order.
        # and appending it to the above process_list.
        process_list.append(purchase_order.process_set.all())


    data = { 
        'purchase_orders': zip(purchase_orders,process_list),
        'user_role': user_role
    }
    return render(request,'purchase_order_management/client_detail_view.html',data)

@login_required
def vendor_list(request):
    """Generates the list of all the vendors.
    Parameters: HttpRequest object
    Returns : Nothing"""
    user_role = request.user.user_role
    # Get all the clients.
    vendors = Vendor.objects.all()
    vendors_total_amount = {}
    vendors_total_amount_due = {}
    for vendor in vendors:
        total_amount = 0
        total_amount_due = 0
        for process in vendor.process_set.all():
            total_amount += process.process_amount
            total_amount_due += process.process_amount_due
        vendors_total_amount[vendor.pk]=total_amount
        vendors_total_amount_due[vendor.pk]=total_amount_due
    data = {
        'vendors': vendors,
        'vendors_total_amount': vendors_total_amount,
        'vendors_total_amount_due': vendors_total_amount_due,
        'user_role': user_role
     }
    return render(request, 'purchase_order_management/vendor_list.html', data )

@login_required
def vendor_list_details(request, pk):
    user_role = request.user.user_role
    vendor = Vendor.objects.get(pk=pk)
    processes = vendor.process_set.all()

    data = { 
        'processes':processes,
        'user_role': user_role
    }
    return render(request,'purchase_order_management/vendor_detail_view.html',data)

@login_required
def home(request):
    data = { }
    return render(request, 'home.html', data )

@login_required
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

@login_required
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


@login_required
def user_list(request):
    user_role = request.user.user_role
    users = CustomUser.objects.all()
    data = { 'users' : users, 'user_role': user_role }
    return render(request, 'purchase_order_management/user_list.html',data)

@login_required
def report_error(request):
    """Form for taking User Errors
    Parameters: HttpRequest object
    Returns : Nothing"""
    user_role = request.user.user_role
    data = { 'user_role': user_role}
    return render(request, 'purchase_order_management/report_error.html', data )


def error_404(request,exception):
    data = { }
    return render(request, 'purchase_order_management/404.html', data )

def error_500(request):
    data = { }
    return render(request, 'purchase_order_management/500.html', data )

@login_required
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
                                    process_amount = process_amount, process_amount_due = process_amount,paper_quantity = paper_quantity,
                                    paper_color = paper_color, paper_gsm = paper_gsm,
                                     paper_number_of_sheets = paper_number_of_sheets,
                                     paper_rate = paper_rate,process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)

        if request.POST.get('binding_checkbox', False) == 'binding':
            binding_pf = request.POST['binding_pf']
            binding_type = request.POST['binding_type']
            binding_product = request.POST['binding_product']
            binding_quantity = request.POST['binding_quantity']
            binding_binding_type = request.POST['binding_binding_type']
            binding_rate = request.POST['binding_rate']


            process_name = 'Binding'
            process_vendor_id = Vendor.objects.get(pk=request.POST['binding_vendor'])
            process_size = request.POST['binding_size']
            process_amount = float(binding_rate)*int(binding_quantity)

            binding = Binding.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,binding_quantity = binding_quantity,
                                    binding_pf = binding_pf, binding_type = binding_type,
                                    binding_product = binding_product, binding_binding_type = binding_binding_type,
                                    binding_rate = binding_rate, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)

        
        if request.POST.get('ctp_checkbox', False) == 'ctp':
            ctp_type = request.POST['ctp_type']
            ctp_number_of_plates = request.POST['ctp_number_of_plates']
            ctp_rate = request.POST['ctp_rate']
            ctp_quantity = request.POST['ctp_quantity']

            process_name = 'CTP'
            process_vendor_id = Vendor.objects.get(pk=request.POST['ctp_vendor'])
            process_size = request.POST['ctp_size']
            process_amount = float(ctp_rate)*int(ctp_quantity)

            ctp = CTP.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    ctp_type = ctp_type, ctp_number_of_plates = ctp_number_of_plates, ctp_rate = ctp_rate,
                                    ctp_quantity = ctp_quantity, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)

        
        if request.POST.get('specialprocess_checkbox', False) == 'specialprocess':
            specialprocess_type = request.POST['specialprocess_type']
            specialprocess_impression = request.POST['specialprocess_impression']
            specialprocess_rate = request.POST['specialprocess_rate']
            specialprocess_quantity = request.POST['specialprocess_quantity']

            process_name = 'Special Process'
            process_vendor_id = Vendor.objects.get(pk=request.POST['specialprocess_vendor'])
            process_size = request.POST['specialprocess_size']
            process_amount = float(specialprocess_rate)*float(specialprocess_impression)

            specialprocess = SpecialProcess.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    specialprocess_type = specialprocess_type, specialprocess_impression = specialprocess_impression, specialprocess_rate = specialprocess_rate,
                                    specialprocess_quantity = specialprocess_quantity, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)

        
        if request.POST.get('raiseuv_checkbox', False) == 'raiseuv':
            raiseuv_type = request.POST['raiseuv_type']
            raiseuv_rate = request.POST['raiseuv_rate']
            raiseuv_quantity = request.POST['raiseuv_quantity']
            raiseuv_number_of_sheets = request.POST['raiseuv_number_of_sheets']
            raiseuv_length = request.POST['raiseuv_length']
            raiseuv_breadth = request.POST['raiseuv_breadth']

            process_name = 'Raise UV'
            process_vendor_id = Vendor.objects.get(pk=request.POST['raiseuv_vendor'])
            process_size = request.POST['raiseuv_size']
            process_amount = float(raiseuv_rate)*float(raiseuv_length)*float(raiseuv_breadth)*int(raiseuv_quantity)*0.01

            raiseuv = RaiseUV.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    raiseuv_type = raiseuv_type, raiseuv_rate = raiseuv_rate,
                                    raiseuv_quantity = raiseuv_quantity, raiseuv_number_of_sheets = raiseuv_number_of_sheets,raiseuv_length = raiseuv_length ,raiseuv_breadth = raiseuv_breadth, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)

            
        if request.POST.get('varnish_checkbox', False) == 'varnish':
            varnish_type = request.POST['varnish_type']
            varnish_rate = request.POST['varnish_rate']
            varnish_quantity = request.POST['varnish_quantity']
            varnish_number_of_sheets = request.POST['varnish_number_of_sheets']
            varnish_length = request.POST['varnish_length']
            varnish_breadth = request.POST['varnish_breadth']

            process_name = 'Varnish'
            process_vendor_id = Vendor.objects.get(pk=request.POST['varnish_vendor'])
            process_size = request.POST['varnish_size']
            process_amount = float(varnish_rate)*float(varnish_length)*float(varnish_breadth)*int(varnish_quantity)*0.01

            varnish = Varnish.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    varnish_type = varnish_type, varnish_rate = varnish_rate,
                                    varnish_quantity = varnish_quantity, varnish_number_of_sheets = varnish_number_of_sheets,varnish_length = varnish_length ,varnish_breadth = varnish_breadth, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)

        if request.POST.get('lamination_checkbox', False) == 'lamination':
            lamination_type = request.POST['lamination_type']
            lamination_rate = request.POST['lamination_rate']
            lamination_quantity = request.POST['lamination_quantity']
            lamination_number_of_sheets = request.POST['lamination_number_of_sheets']
            lamination_length = request.POST['lamination_length']
            lamination_breadth = request.POST['lamination_breadth']

            process_name = 'Lamination'
            process_vendor_id = Vendor.objects.get(pk=request.POST['lamination_vendor'])
            process_size = request.POST['lamination_size']
            process_amount = float(lamination_rate)*float(lamination_length)*float(lamination_breadth)*int(lamination_quantity)*0.01

            lamination = Lamination.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    lamination_type = lamination_type, lamination_rate = lamination_rate,
                                    lamination_quantity = lamination_quantity, lamination_number_of_sheets = lamination_number_of_sheets,lamination_length = lamination_length ,lamination_breadth = lamination_breadth, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)

        if request.POST.get('positive_checkbox', False) == 'positive':
            positive_type = request.POST['positive_type']
            positive_rate = request.POST['positive_rate']
            positive_quantity = request.POST['positive_quantity']
            positive_number_of_sheets = request.POST['positive_number_of_sheets']
            positive_length = request.POST['positive_length']
            positive_breadth = request.POST['positive_breadth']

            process_name = 'Positive'
            process_vendor_id = Vendor.objects.get(pk=request.POST['positive_vendor'])
            process_size = request.POST['positive_size']
            process_amount = float(positive_rate)*float(positive_length)*float(positive_breadth)*int(positive_quantity)*0.01

            positive = Positive.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    positive_type = positive_type, positive_rate = positive_rate,
                                    positive_quantity = positive_quantity, positive_number_of_sheets = positive_number_of_sheets,positive_length = positive_length ,positive_breadth = positive_breadth, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)
        


        if request.POST.get('printing_checkbox', False) == 'printing':
            printing_rate = request.POST['printing_rate']
            printing_quantity = request.POST['printing_quantity']
            printing_number_of_cols = request.POST['printing_number_of_cols']
            printing_detail = request.POST['printing_detail']
            printing_rate = request.POST['printing_rate']
            printing_impression = request.POST['printing_impression']

            process_name = 'Printing'
            process_vendor_id = Vendor.objects.get(pk=request.POST['printing_vendor'])
            process_size = request.POST['printing_size']
            process_amount = float(printing_rate)*float(printing_impression)

            printing = Printing.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    printing_rate = printing_rate, printing_quantity = printing_quantity, 
                                    printing_number_of_cols = printing_number_of_cols, printing_detail = printing_detail ,printing_impression = printing_impression, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)


        if request.POST.get('cutting_checkbox', False) == 'cutting':
            cutting_rate = request.POST['cutting_rate']
            cutting_quantity = request.POST['cutting_quantity']
            cutting_paper = request.POST['cutting_paper']
            cutting_rate = request.POST['cutting_rate']

            process_name = 'Cutting'
            process_vendor_id = Vendor.objects.get(pk=request.POST['cutting_vendor'])
            process_size = request.POST['cutting_size']
            process_amount = float(cutting_rate)*int(cutting_quantity)

            cutting = Cutting.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    cutting_rate = cutting_rate, cutting_quantity = cutting_quantity, 
                                    cutting_paper = cutting_paper, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)

        
        if request.POST.get('punching_checkbox', False) == 'punching':
            punching_rate = request.POST['punching_rate']
            punching_quantity = request.POST['punching_quantity']
            punching_impression = request.POST['punching_impression']
            punching_rate = request.POST['punching_rate']

            process_name = 'Punching'
            process_vendor_id = Vendor.objects.get(pk=request.POST['punching_vendor'])
            process_size = request.POST['punching_size']
            process_amount = float(punching_rate)*float(punching_impression)

            punching = Punching.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    punching_rate = punching_rate, punching_quantity = punching_quantity, 
                                    punching_impression = punching_impression, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)

        
        if request.POST.get('pasting_checkbox', False) == 'pasting':
            pasting_rate = request.POST['pasting_rate']
            pasting_quantity = request.POST['pasting_quantity']
            pasting_impression = request.POST['pasting_impression']
            pasting_rate = request.POST['pasting_rate']
            pasting_number_of_pasting = request.POST['pasting_number_of_pasting']

            process_name = 'Pasting'
            process_vendor_id = Vendor.objects.get(pk=request.POST['pasting_vendor'])
            process_size = request.POST['pasting_size']
            process_amount = float(pasting_rate)*float(pasting_impression)

            pasting = Pasting.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    pasting_rate = pasting_rate, pasting_quantity = pasting_quantity, 
                                    pasting_impression = pasting_impression, process_vendor_id = process_vendor_id, pasting_number_of_pasting = pasting_number_of_pasting, process_purchase_order_id = purchase_order)

        if request.POST.get('folding_checkbox', False) == 'folding':
            folding_rate = request.POST['folding_rate']
            folding_quantity = request.POST['folding_quantity']
            folding_impression = request.POST['folding_impression']
            folding_rate = request.POST['folding_rate']
            folding_number_of_folds = request.POST['folding_number_of_folds']

            process_name = 'Folding'
            process_vendor_id = Vendor.objects.get(pk=request.POST['folding_vendor'])
            process_size = request.POST['folding_size']
            process_amount = float(folding_rate)*float(folding_impression)

            folding = Folding.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    folding_rate = folding_rate, folding_quantity = folding_quantity, 
                                    folding_impression = folding_impression, process_vendor_id = process_vendor_id, folding_number_of_folds = folding_number_of_folds, process_purchase_order_id = purchase_order)

        if request.POST.get('creasing_checkbox', False) == 'creasing':
            creasing_rate = request.POST['creasing_rate']
            creasing_quantity = request.POST['creasing_quantity']
            creasing_impression = request.POST['creasing_impression']

            process_name = 'Creasing'
            process_vendor_id = Vendor.objects.get(pk=request.POST['creasing_vendor'])
            process_size = request.POST['creasing_size']
            process_amount = float(creasing_rate)*float(creasing_impression)

            creasing = Creasing.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    creasing_rate = creasing_rate, creasing_quantity = creasing_quantity, 
                                    creasing_impression = creasing_impression, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)


        if request.POST.get('punch_checkbox', False) == 'punch':
            punch_number_of_sheets = request.POST['punch_number_of_sheets']

            process_name = 'Punch'
            process_vendor_id = Vendor.objects.get(pk=request.POST['punch_vendor'])
            process_size = request.POST['punch_size']
            process_amount = request.POST['punch_amount']

            punch = Punch.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    punch_number_of_sheets = punch_number_of_sheets, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)


        if request.POST.get('block_checkbox', False) == 'block':
            block_number_of_sheets = request.POST['block_number_of_sheets']

            process_name = 'Block'
            process_vendor_id = Vendor.objects.get(pk=request.POST['block_vendor'])
            process_size = request.POST['block_size']
            process_amount = request.POST['block_amount']

            block = Block.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    block_number_of_sheets = block_number_of_sheets, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)


        if request.POST.get('fourcol_checkbox', False) == 'fourcol':
            fourcol_for = request.POST['fourcol_for']
            fourcol_type = request.POST['fourcol_type']
            fourcol_rate = request.POST['fourcol_rate']
            fourcol_unit = request.POST['fourcol_unit']

            process_name = 'FourCol'
            process_vendor_id = Vendor.objects.get(pk=request.POST['fourcol_vendor'])
            process_size = request.POST['fourcol_size']
            process_amount = float(fourcol_rate)*float(fourcol_unit)*1000

            fourcol = FourCol.objects.create(process_name = process_name, process_size = process_size,
                                    process_amount = process_amount, process_amount_due = process_amount,
                                    fourcol_rate = fourcol_rate,fourcol_for = fourcol_for, fourcol_type = fourcol_type,
                                    fourcol_unit = fourcol_unit, process_vendor_id = process_vendor_id, process_purchase_order_id = purchase_order)



    return HttpResponseRedirect(reverse('purchase_order_management:purchase_order_list'))

def purchase_order_summary(request,purchase_order_id):
    user_role = request.user.user_role
    user_name = request.user.username

    # Get Purchase Order Object as per Purchase Order Id Passed
    purchase_order = PurchaseOrder.objects.get(pk=purchase_order_id)
    # Generate the list of processes for Purchase Order Id Passed
    processes = Process.objects.filter(process_purchase_order_id=purchase_order_id).select_subclasses()
    process_list = list(processes)
    process_dict = {}
    cost_price = 0
    for process in processes:
        process_dict[process.process_name] = process
        cost_price += process.process_amount
    profit_loss = purchase_order.purchase_order_amount - cost_price
    # Generate Summary Dictionary
    summary_dict = {
        'selling_price': purchase_order.purchase_order_amount,
        'cost_price': cost_price,
        'profit_loss': profit_loss,
    }
    data = {
        'purchase_order': purchase_order,
        'user_role': user_role,
        'user_name': user_name,
        'process': process_dict,
        'Summary': summary_dict,
     }
    return render(request, 'purchase_order_management/purchase_order_summary.html', data )