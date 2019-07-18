from django.contrib import admin
from django.urls import path
from purchase_order_management import views

app_name = 'purchase_order_management'
urlpatterns = [
    # url for temporary home page
    path('', views.home, name = 'home'),
    # url for purchase form
    path('purchase_order_form/', views.purchase_form, name = 'purchase_order_form'),
    # url for purchase order list
    path('purchase_order_list/', views.purchase_list, name = 'purchase_order_list'),

    # url for purchase order list delete modal
    path('delete_purchase_order_list/<int:pk>', views.PurchaseOrderDeleteView.as_view(), name='delete_purchase_order_list'),

]