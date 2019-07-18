from django.contrib import admin
from django.contrib.auth.models import Group, User
from purchase_order_management.models import CustomUser, Vendor, Process,PurchaseOrder, Paper, Cutting

# Register your models here.
admin.site.unregister(Group)
admin.site.register(CustomUser)
admin.site.register(PurchaseOrder)
admin.site.register(Vendor)
admin.site.register(Process)
admin.site.register(Paper)
admin.site.register(Cutting)

