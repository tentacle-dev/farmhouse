from django.urls import path
from . import views

urlpatterns = [
    path('admin1', views.admin1, name="admin1"),

    path('view_customers', views.view_customers, name="view_customers"),
    path('view_sellers', views.view_sellers, name="view_sellers"),
    path('delete_user/<int:id>', views.delete_user, name="delete_user"),
    path('accept_seller/<int:id>', views.accept_seller, name="accept_seller"),
    path('accept_seller1', views.accept_seller1, name="accept_seller1"),

    path('user_history/<int:id>', views.user_history, name="user_history"),

    path('view_order_admin', views.view_order_admin, name="view_order_admin"),
    path('view_order_admin_post', views.view_order_admin_post, name="view_order_admin_post"),
    path('customer_order_details_admin/<int:id>', views.customer_order_details_admin, name="customer_order_details_admin"),

    path('view_transaction', views.view_transaction, name="view_transaction"),
    path('view_transaction_customer/<int:id>', views.view_transaction_customer, name="view_transaction_customer"),
    path('view_transaction_post', views.view_transaction_post, name="view_transaction_post"),

    path('view_customer_feedback', views.view_customer_feedback, name="view_customer_feedback"),
    path('view_seller_feedback', views.view_seller_feedback, name="view_seller_feedback"),
    
     path('seller_products/<int:id>', views.seller_products, name="seller_products"),
]