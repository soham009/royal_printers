from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    '''Overrides the custom django user model'''
    # Datafields
    SUPER_ADMIN = 1
    ADMIN = 2
    ROLE_CHOICES = (
      (ADMIN,'admin'),
      (SUPER_ADMIN,'super_admin')
    )
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=ADMIN)

class Vendor(models.Model):

    # DataFields
    vendor_name = models.CharField(max_length=200)
    vendor_address = models.CharField(max_length=400)
    vendor_total_amount = models.FloatField()
    vendor_amount_due  = models.FloatField()

    def __str__(self):
        return str(self.pk)

class Client(models.Model):

    client_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.pk)

class Process(models.Model):

    # Datafields
    process_name = models.CharField(max_length=100)
    process_created_on = models.DateTimeField(auto_now_add=True)
    process_updated_on = models.DateTimeField(auto_now=True)
    process_size = models.CharField(max_length=100)
    process_amount = models.FloatField()

    # Relationship of process with vendor
    process_vendor_id = models.ForeignKey(Vendor, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.pk)

class Paper(Process):

    # DataFields
    paper_color = models.CharField(max_length=100)
    paper_gsm = models.CharField(max_length = 100)
    paper_number_of_sheets = models.IntegerField()
    paper_quantity = models.IntegerField()
    paper_rate = models.FloatField()

    def __str__(self):
        return str(self.pk)+" "+str(self.paper_rate)

class Printing(Process):

    # DataFields
    printing_quantity = models.IntegerField()
    printing_detail = models.CharField(max_length=300)
    printing_no_of_cols = models.IntegerField()
    printing_impression = models.FloatField()
    printing_rate = models.FloatField()

    def __str__(self):
        return str(self.pk)

class Binding(Process):

    # DataFields
    binding_pf = models.CharField(max_length=100)
    SIDE = 'side'
    TOP = 'top'
    TYPE_CHOICES = (
        (SIDE,'side'),
        (TOP,'top')
    )
    binding_type = models.CharField(choices=TYPE_CHOICES,max_length=100)

    BOOK = 'book'
    PAD = 'pad'
    
    PRODUCT_CHOICES = (
        (BOOK,'book'),
        (PAD,'pad')
    )
    binding_product = models.CharField(choices=PRODUCT_CHOICES,max_length=100)

    binding_quantity = models.IntegerField()

    SADA = 'sada'
    DP = 'dp'
    THREEFOLD = 'threefold'
    REXIN = 'rexin'
    CLOTH = 'cloth'
    PACKET = 'packet'
    CUSTOM = 'custom'
    BINDING_TYPE_CHOICES = (
        (SADA,'sada'),
        (DP,'dp'),
        (THREEFOLD,'threefold'),
        (REXIN,'rexin'),
        (CLOTH,'cloth'),
        (PACKET,'packet'),
        (CUSTOM,'custom'),
    )
    binding_binding_type = models.CharField(choices=BINDING_TYPE_CHOICES,max_length=100)

    binding_rate = models.FloatField()

    def __str__(self):
        return str(self.pk)

class Lamination(Process):

    # DataFields
    PVC = 'pvc'
    BOPP = 'bopp'
    MATT = 'matt'
    THERMAL = 'thermal'
    CUSTOM = 'custom'

    LAMINATION_CHOICES = (
    (PVC,'pvc'),
    (BOPP,'bopp'),
    (MATT,'matt'),
    (THERMAL,'thermal'),
    (CUSTOM,'custom')
    )
    lamination_type = models.CharField(choices=LAMINATION_CHOICES,max_length=100)

    lamination_size = models.CharField(max_length=100)
    lamination_no_of_sheets = models.IntegerField()
    lamination_quantity = models.IntegerField()
    lamination_length = models.FloatField()
    lamination_breadth = models.FloatField()
    lamination_rate = models.FloatField()

    def __str__(self):
        return str(self.pk)

class RaiseUV(Process):

    # DataFields
    PVC = 'pvc'
    BOPP = 'bopp'
    MATT = 'matt'
    THERMAL = 'thermal'
    CUSTOM = 'custom'

    RAISEUV_CHOICES = (
    (PVC,'pvc'),
    (BOPP,'bopp'),
    (MATT,'matt'),
    (THERMAL,'thermal'),
    (CUSTOM,'custom')
    )
    raiseuv_type = models.CharField(choices= RAISEUV_CHOICES,max_length=100)

    raiseuv_size = models.CharField(max_length=100)
    raiseuv_no_of_sheets = models.IntegerField()
    raiseuv_quantity = models.IntegerField()
    raiseuv_length = models.FloatField()
    raiseuv_breadth = models.FloatField()
    raiseuv_rate = models.FloatField()

    def __str__(self):
        return str(self.pk)

class Varnish(Process):

    #DataFields
    PVC = 'pvc'
    BOPP = 'bopp'
    MATT = 'matt'
    THERMAL = 'thermal'
    CUSTOM = 'custom'

    VARNISH_CHOICES = (
    (PVC,'pvc'),
    (BOPP,'bopp'),
    (MATT,'matt'),
    (THERMAL,'thermal'),
    (CUSTOM,'custom')
    )
    varnish_type = models.CharField(choices= VARNISH_CHOICES,max_length=100)

    varnish_size = models.CharField(max_length=100)
    varnish_no_of_sheets = models.IntegerField()
    varnish_quantity = models.IntegerField()
    varnish_length = models.FloatField()
    varnish_breadth = models.FloatField()
    varnish_rate = models.FloatField()

    def __str__(self):
        return str(self.pk)
        
class Positive(Process):
    # DataFields
    PVC = 'pvc'
    BOPP = 'bopp'
    MATT = 'matt'
    THERMAL = 'thermal'
    CUSTOM = 'custom'

    POSITIVE_CHOICES = (
    (PVC,'pvc'),
    (BOPP,'bopp'),
    (MATT,'matt'),
    (THERMAL,'thermal'),
    (CUSTOM,'custom')
    )
    positive_type = models.CharField(choices= POSITIVE_CHOICES,max_length=100)

    positive_size = models.CharField(max_length=100)
    positive_no_of_sheets = models.IntegerField()
    positive_quantity = models.IntegerField()
    positive_length = models.FloatField()
    positive_breadth = models.FloatField()
    positive_rate = models.FloatField()

    def __str__(self):
        return str(self.pk)

class CTP(Process):

    # DataFields
    NEW = 'new'
    OLD = 'old'
    ctp_size = models.CharField(max_length=100)
    CTP_TYPE = (
        (NEW,'new'),
        (OLD,'old')
    )
    ctp_type = models.CharField(choices=CTP_TYPE, max_length=100)
    ctp_no_of_plates = models.IntegerField()
    ctp_rate = models.FloatField()
    ctp_quantity = models.FloatField()


    def __str__(self):
        return str(self.pk)

class Cutting(Process):

    #DataFields
    cutting_size = models.CharField(max_length=100)
    cutting_quantity = models.CharField(max_length=100)
    cutting_paper = models.CharField(max_length=100)
    cutting_rate = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk)

class Folding(Process):

    # DataFields
    folding_no_of_folds = models.IntegerField()
    folding_quantity = models.IntegerField()
    folding_rate = models.IntegerField()
    folding_impression = models.IntegerField()

    def __str__(self):
        return str(self.pk)

class Pasting(Process):

    # DataFields
    pasting_impression = models.FloatField()
    pasting_size = models.CharField(max_length=100)
    pasting_no_of_pasting = models.IntegerField()
    pasting_quantity = models.IntegerField()
    pasting_rate = models.FloatField()

    def __str__(self):
        return str(self.pk)

class Creasing(Process):

    # DataFields
    creasing_impression = models.FloatField()
    creasing_size = models.CharField(max_length=100)
    creasing_quantity = models.IntegerField()
    creasing_rate = models.FloatField()

    def __str__(self):
        return str(self.pk)

class Punch(Process):


    # DataFields
    punch_size = models.CharField(max_length=100)
    punch_no_of = models.IntegerField()

    def __str__(self):
        return str(self.pk)

class Block(Process):
    # DataFields
    block_size = models.CharField(max_length=100)
    block_no_of = models.IntegerField()

    def __str__(self):
        return str(self.pk)

class Punching(Process):

    # DataFields
    punching_size = models.CharField(max_length=100)
    punching_quantity = models.IntegerField()
    punching_impression = models.FloatField()
    punching_rate = models.FloatField()

    def __str__(self):
        return str(self.pk)

class FourCol(Process):

    # DataFields
    VCARD = 'vcard'
    LHEADS = 'lheads'
    ENV = 'env'
    PAMP = 'pamp'

    FOR_CHOICES = (
        (VCARD,'vcard'),
        (LHEADS,'lheads'),
        (ENV,'env'),
        (PAMP,'pamp')
    )
    fourcol_for = models.CharField(choices=FOR_CHOICES, max_length=100)
    fourcol_size = models.FloatField()
    
    SINGLE = 'single'
    FRONTBACK = 'frontback'
    TYPE_CHOICES = (
        (SINGLE,'single'),
        (FRONTBACK,'frontback'),
    )
    fourcol_type = models.CharField(choices=TYPE_CHOICES, max_length=100)
    fourcol_rate = models.FloatField()
    fourcol_unit = models.IntegerField()


    def __str__(self):
        return str(self.pk)

class SpecialProcess(Process):
    #DataFields
    EMBOSSING = 'embossing'
    DEBOSSING = 'debossing'
    FOILING = 'foiling'

    TYPE_CHOICES = (
        (EMBOSSING,'embossing'),
        (DEBOSSING,'debossing'),
        (FOILING, 'foiling')
    )
    special_process_type = models.CharField(choices=TYPE_CHOICES, max_length=100)
    specialprocess_quantity = models.IntegerField()
    specialprocess_impression = models.FloatField()
    specialprocess_size = models.CharField(max_length=100)
    specialprocess_rate = models.FloatField()

    def __str__(self):
        return str(self.pk)
    

class PurchaseOrder(models.Model):
    # DataFields
    purchase_order_item = models.CharField(max_length=200)
    purchase_order_item_quantity = models.IntegerField()
    purchase_order_size = models.CharField(max_length=200)
    purchase_order_number_of_columns = models.IntegerField(blank=True)
    purchase_order_created_on = models.DateTimeField(auto_now_add=True)
    purchase_order_updated_on = models.DateTimeField(auto_now=True)
    purchase_order_purchase_date = models.DateField()
    purchase_order_purchase_by = models.DateField()
    purchase_order_name = models.CharField(max_length=200)
    purchase_order_po_number = models.IntegerField()
    purchase_order_number = models.IntegerField()
    purchase_order_amount = models.FloatField()
    purchase_order_amount_due = models.FloatField()

    # Relation with the user,client  and the processes.
    purchase_order_user_id = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    purchase_order_client_id = models.ForeignKey(Client, on_delete= models.CASCADE)
    purchase_order_process_relation = models.ManyToManyField(Process)
    

    def __str__(self):
        return str(self.pk)+" "+str(self.purchase_order_client_id)
    


