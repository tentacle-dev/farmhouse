from django.shortcuts import render

from customer.models import Cart, Payment
from seller.models import Product
from login.models import User, Login, Feedback


def admin1(request):
    role = request.session["role"]
    if role==0:
        return render(request,'admin/admin.html')
    user = User.objects.get(loginid_id=request.session['userid'])
    if role==1:
       user = User.objects.get(loginid_id=request.session['userid'])
       uid = user.id
       p = Product.objects.filter(userid=uid)
       return render(request, 'seller/product_dashs.html', {'p': p,'user':user})
    else:
        user = User.objects.get(loginid_id=request.session['userid'])
        p = Product.objects.all()
        return render(request, 'customer/customer.html', {'p': p,'user':user})

def delete_user(request,id):
    u=User.objects.get(id=id)
    log = u.loginid_id
    role=u.role
    l = Login.objects.get(id=log)
    u.delete()
    l.delete()
    if role == 1:
        users = User.objects.raw('SELECT * from login_user where role=1 and status="accept" ')
        return render(request, "admin/user_table.html", {'users': users})
    if role == 2:
        users = User.objects.raw('SELECT * from login_user where role=2')
        return render(request, "admin/user_table.html", {'users': users})

def accept_seller(request,id):
    l=User.objects.get(id=id)
    l.status="accept"
    l.save()
    users =User.objects.raw('SELECT * from login_user where status="not" order by date desc')
    return render(request, "admin/accept_seller_table.html", {'users': users})

def accept_seller1(request):
    users =User.objects.raw('SELECT * from login_user where status="not" order by date desc')
    return render(request, "admin/accept_seller_table.html", {'users': users})

def view_sellers(request):
    users = User.objects.raw('SELECT * from login_user where role=1 and status="accept"')
    return render(request, "admin/user_table.html", {'users': users,'table':'Seller Details'})

def view_customers(request):
    users = User.objects.raw('SELECT * from login_user where role=2')
    return render(request, "admin/user_table.html", {'users': users,'table':'Customer Details'})


def view_customer_feedback(request):
    users = Feedback.objects.raw('SELECT * from login_feedback where role=2 order by date desc')
    return render(request, "admin/user_feedback.html", {'users': users,'feed':'Customer Feedback'})

def view_seller_feedback(request):
    users = Feedback.objects.raw('SELECT * from login_feedback  where role=1 order by date desc')
    return render(request, "admin/user_feedback.html", {'users': users,'feed':'Seller Feedback'})

def user_history(request,id):
    uid = User.objects.get(id=id)
    name = uid.name
    if uid.role==1:
        p = Cart.objects.filter(sid=uid, status1='buy',status2='accepted')
        total = 0
        for i in p:
            total = total + int(i.price)
        return render(request, 'admin/seller_history.html',{'p':p,'name':name,'total':total})

    if uid.role==2:
        p = Cart.objects.filter(cid=uid, status1='buy',status2='accepted')
        total = 0
        for i in p:
            total = total + int(i.price)
        return render(request, 'admin/customer_history.html',{'p':p,'name':name,'total':total})

def view_order_admin(request):
    users = Cart.objects.raw('select * from customer_cart where status1="buy" and status2="accepted" order by sdate desc')
    total=0
    for i in users:
        total = total + int(i.price)
    return render(request, 'admin/view_order_admin.html', {'users': users,'total':total})

def view_order_admin_post(request):
    if request.method=='POST':
        mo = request.POST.get("month")
        ye = request.POST.get("year")
        users = Cart.objects.raw('select * from customer_cart where year(sdate)=%s and month(sdate)=%s and status1="buy" and status2="accepted"order by sdate desc',(ye,mo))
        total=0
        for i in users:
            total = total + int(i.price)
        return render(request, 'admin/view_order_admin.html', {'users': users, 'total': total})

def customer_order_details_admin(request,id):
    p = Cart.objects.get(id=id)
    role = request.session["role"]
    return render(request, 'seller/customer_order_details.html', {'p': p,'role':role})



def view_transaction(request):
    p = Payment.objects.all()
    total = 0
    for i in p:
        total = total + int(i.money)
    return render(request, 'admin/view_transaction.html', {'p': p,'total': total})

def view_transaction_customer(request,id):
    p = Payment.objects.get(id=id)
    u=p.pcid
    d=p.date
    user=Cart.objects.filter(sdate=d,cid=u,status1="buy")

    name = p.pcid.name
    total = p.money
    return render(request, 'admin/view_transaction_customer.html', {'users': user,'total': total,'name':name})

def view_transaction_post(request):
    if request.method == 'POST':
        mo = request.POST.get("month")
        ye = request.POST.get("year")
        users = Payment.objects.raw(
            'select * from customer_payment where year(date)=%s and month(date)=%s order by date desc',
            (ye, mo))
        total = 0
        for i in users:
            total = total + int(i.money)
        return render(request, 'admin/view_transaction.html', {'p': users, 'total': total})
    
    

def seller_products(request,id):
    user = User.objects.get(loginid_id=id)
    uid = user.id
    p = Product.objects.filter(userid=uid)
    return render(request, 'admin/seller_products.html', {'p': p,'user':user})