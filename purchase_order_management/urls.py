from django.contrib import admin
from django.urls import path, re_path
from purchase_order_management import views

app_name = 'purchase_order_management'
urlpatterns = [
    # url for sign in page
    path('', views.user_sign_in, name = 'sign_in'),

    # url for sign up page
    path('sign_up/', views.user_sign_up, name = 'sign_up'),

    # url for sign out view
    path('sign_out/', views.user_sign_out, name = 'sign_out'),

    # url for users list
    path('user_list/', views.user_list, name = 'user_list'),

    #url for users list update modal
    path('user_list/update/<int:pk>', views.CustomUserUpdateView.as_view(), name = 'update_user_list'),

    # url for purchase form
    path('purchase_order_form/', views.purchase_order_form, name = 'purchase_order_form'),
    # url for purchase order list
    path('purchase_order_list/', views.purchase_list, name = 'purchase_order_list'),

    # url for purchase order list delete modal
    path('delete_purchase_order_list/<int:pk>/', views.PurchaseOrderDeleteView.as_view(), name='delete_purchase_order_list'),

    # url for purchase order list update modal
    path('update_purchase_order_list/<int:pk>/', views.PurchaseOrderUpdateView.as_view(), name='update_purchase_order_list'),

    
    # url for purchase order detail view
    path('purchase_order_list/detail/<int:pk>', views.purchase_order_list_details, name ='purchase_order_list_detail'),

    # url for client list
    path('client_list/', views.client_list, name ='client_list'),
    
    # url for client list create modal
    path('create_client_list/', views.ClientCreateView.as_view(), name ='create_client_list'),

    # url for client detail view
    path('client_list/detail/<int:pk>', views.client_list_details, name ='client_list_detail'),


    # url for process list
    path('process_list/', views.process_list, name ='process_list'),

    
    # url for process list delete modal
    path('delete_process_list/<int:pk>/', views.ProcessDeleteView.as_view(), name='delete_process_list'),

    # url for process list update modal
    path('update_process_list/<int:pk>/', views.ProcessUpdateView.as_view(), name='update_process_list'),

    # url for purchase order list detail update modal
    path('update_process_list_purchase_order_detail/<int:pk>/', views.PurchaseOrderProcessDetailUpdateView.as_view(), name='update_process_list_purchase_order_detail'),
    # url for purchase order list detail delete modal
    path('delete_process_list_purchase_order_detail/<int:pk>/', views.PurchaseOrderProcessDetailDeleteView.as_view(), name='delete_process_list_purchase_order_detail'),


    # url for purchase order list detail update modal
    path('update_process_list_vendor_detail/<int:pk>/', views.VendorProcessDetailUpdateView.as_view(), name='update_process_list_vendor_detail'),
    # url for purchase order list detail delete modal
    path('delete_process_list_vendor_detail/<int:pk>/', views.VendorProcessDetailDeleteView.as_view(), name='delete_process_list_vendor_detail'),

    # url for client purchase order list detail update modal
    path('update_purchase_order_list_client_detail/<int:pk>/', views.ClientPurchaseOrderDetailUpdateView.as_view(), name='update_purchase_order_list_client_detail'),
    # url for client purchase order list detail delete modal
    path('delete_purchase_order_list_client_detail/<int:pk>/', views.ClientPurchaseOrderDetailDeleteView.as_view(), name='delete_purchase_order_list_client_detail'),
    
    # url for vendor list
    path('vendor_list/', views.vendor_list, name ='vendor_list'),

    # url for vendor list create modal
    path('create_vendor_list/', views.VendorCreateView.as_view(), name ='create_vendor_list'),

    # url for vendor detail view
    path('vendor_list/detail/<int:pk>', views.vendor_list_details, name ='vendor_list_detail'),

    # url for submitting purchase order form
    path('purchase_order_form/submit/', views.purchase_order_form_submit, name='purchase_order_form_submit'),

    # url for profile page
    path('my_profile/', views.profile, name ='profile'),

    # url for report error page
    path('report_error/', views.report_error, name ='report_errors'),

     # url for Purchase Order Form
    path('purchase_order_summary/<int:purchase_order_id>/', views.purchase_order_summary, name='order_summary'),


]