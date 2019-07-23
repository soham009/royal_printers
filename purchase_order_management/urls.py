from django.contrib import admin
from django.urls import path
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

    # url for client list
    path('client_list/', views.client_list, name ='client_list'),

    # url for client list update modal
    path('update_client_list/<int:pk>/', views.ClientUpdateView.as_view(), name='update_client_list'),

    
    # url for vendor list
    path('vendor_list/', views.vendor_list, name ='vendor_list'),

    # url for vendor list update modal
    path('update_vendor_list/<int:pk>/', views.VendorUpdateView.as_view(), name='update_vendor_list'),

    path('error_404/', views.error_404, name ='error_404'),
    path('my_profile/', views.profile, name ='profile'),
    path('report_error/', views.report_error, name ='report_errors'),

]