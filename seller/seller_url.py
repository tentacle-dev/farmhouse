from django.urls import path
from . import views

urlpatterns = [
    path('seller', views.seller, name="seller"),
    path('insert_product', views.insert_product, name="insert_product"),
    path('update_product/<int:id>', views.update_product, name="update_product"),
    path('view_product/<int:id>', views.view_product, name="view_product"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),

    path('product_dashs', views.product_dashs, name="product_dashs"),

    path('accept_order', views.accept_order, name="accept_order"),
    path('accept_order_balance/<int:id>', views.accept_order_balance, name="accept_order_balance"),
    path('accept_rejected', views.accept_rejected, name="accept_rejected"),
    path('accept_rejected_balance/<int:id>', views.accept_rejected_balance, name="accept_rejected_balance"),
    path('reject_order/<int:id>', views.reject_order, name="reject_order"),

    path('order_details', views.order_details, name="order_details"),
    path('order_details_post', views.order_details_post, name="order_details_post"),
    path('customer_order_details/<int:id>', views.customer_order_details, name="customer_order_details"),

    path('delete_review/<int:id1>/<int:id2>', views.delete_review, name="delete_review"),
]