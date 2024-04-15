from django.urls import path
from . import views

urlpatterns = [
    path('customer', views.customer, name="customer"),
    path('product_dashc', views.product_dashc, name="product_dashc"),
    path('view_productc/<int:id>', views.view_productc, name="view_productc"),

    path('cart/<int:id>', views.cart, name="cart"),
    path('view_cart', views.view_cart, name="view_cart"),
    path('delete_carted/<int:id>', views.delete_carted, name="delete_carted"),
    path('update_qty/<int:id>', views.update_qty, name="update_qty"),

    path('checkout_single/<int:id>', views.checkout_single, name="checkout_single"),
    path('checkout_single_post/<int:id>', views.checkout_single_post, name="checkout_single_post"),
    path('checkout_group', views.checkout_group, name="checkout_group"),
    path('checkout_group_disp', views.checkout_group_disp, name="checkout_group_disp"),
    path('checkout_single_disp/<int:id>', views.checkout_single_disp, name="checkout_single_disp"),

    path('order_history', views.order_history, name="order_history"),
    path('pending_order', views.pending_order, name="pending_order"),
    path('cancel_order/<int:id>', views.cancel_order, name="cancel_order"),

    path('add_review/<int:id>', views.add_review, name="add_review"),
    
    path('gallery', views.gallery, name="gallery"),
    path('about', views.about, name="about"),
]