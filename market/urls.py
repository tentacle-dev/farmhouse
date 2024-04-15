"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
import adminapp.admin_url
import customer.customer_url
import login.login_url
import seller.seller_url
from market import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminapp/', include(adminapp.admin_url)),
    path('', include(login.login_url)),
    path('seller/', include(seller.seller_url)),
    path('customer/', include(customer.customer_url)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
