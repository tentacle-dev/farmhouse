from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('change_psw', views.change_psw, name="change_psw"),

    path('feedback', views.feedback, name="feedback"),

    path('delete_account', views.delete_account, name="delete_account"),

    path('checkusername/',views.checkusername,name='checkusername'),
    path('checkph/',views.checkph,name='checkph'),

]