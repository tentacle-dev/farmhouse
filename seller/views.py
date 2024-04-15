from django.shortcuts import render


# Create your views here.
from customer.models import Cart, Review
from login.models import User
from seller.models import Product


def seller(request):
    role = request.session["role"]
    user = User.objects.get(loginid_id=request.session['userid'])
    return render(request, 'seller/seller.html',{'user':user,'role':role})


def insert_product(request):
    if request.method == 'POST':
        pname = request.POST.get("pname")
        bname = request.POST.get("bname")
        qty = request.POST.get("qty")
        pd = request.POST.get("pd")
        sprice = request.POST.get("sprice")
        cprice = request.POST.get("cprice")

        if len(request.FILES) != 0:
            pp = request.FILES['pp']
        else:
            pp = 'images/defaultp.jpg'

        o = User.objects.get(loginid_id=request.session['userid'])
        obj = Product()
        obj.userid = o
        obj.pname = pname
        obj.bname = bname
        obj.status = "available"
        obj.qty = qty
        obj.pd = pd
        obj.p_pic = pp
        obj.sprice = sprice
        obj.cprice = cprice
        obj.save()
        p = Product.objects.filter(userid=o)
        return render(request, "seller/product_dashs.html",{'user':o,'p':p})
    user = User.objects.get(loginid_id=request.session['userid'])
    return render(request, 'seller/insert_product.html',{'user':user})

def update_product(request,id):
    if request.method == 'POST':
        obj = Product.objects.get(id=id)
        pname = request.POST.get("pname")
        bname = request.POST.get("bname")
        qty = request.POST.get("qty")
        pd = request.POST.get("pd")
        status=request.POST.get("status")
        sprice = request.POST.get("sprice")
        cprice = request.POST.get("cprice")

        if len(request.FILES) != 0:
            pp = request.FILES['pp']
        else:
            pp=obj.p_pic

        obj.pname = pname
        obj.bname = bname
        obj.status = status
        obj.qty = qty
        obj.pd = pd
        obj.p_pic = pp
        obj.sprice = sprice
        obj.cprice = cprice
        obj.save()
        reviews = Review.objects.filter(pid=id)
        d = int(obj.cprice) - int(obj.sprice)
        user = User.objects.get(loginid_id=request.session['userid'])
        return render(request, 'seller/view_product.html', {'p':obj,'d':d,'user':user,'reviews':reviews})

    p = Product.objects.get(id=id)
    user = User.objects.get(loginid_id=request.session['userid'])
    return render(request, 'seller/update_product.html', {'p': p,'user':user})

def delete_product(request,id):
    user = User.objects.get(loginid_id=request.session['userid'])
    p = Product.objects.get(id=id)
    p.delete()
    uid = user.id
    p = Product.objects.filter(userid=uid)
    return render(request, 'seller/product_dashs.html', {'p': p,'user':user})

def view_product(request,id):
    user = User.objects.get(loginid_id=request.session['userid'])
    p = Product.objects.get(id=id)
    reviews = Review.objects.filter(pid=id)
    d=p.cprice-p.sprice
    return render(request, 'seller/view_product.html',{'p':p,'d':d,'user':user,'reviews':reviews})

def product_dashs(request):
    user = User.objects.get(loginid_id=request.session['userid'])
    uid = user.id
    p = Product.objects.filter(userid=uid)
    return render(request, 'seller/product_dashs.html', {'p': p,'user':user})


def accept_order(request):
    user = User.objects.get(loginid_id=request.session['userid'])
    uid=user.id
    users = Cart.objects.filter(sid=uid, status2="pending",status1="buy")
    return render(request, 'seller/accept_order.html', {'users': users,'user':user})

def accept_order_balance(request,id):
    u = Cart.objects.get(id=id)
    u.status2="accepted"
    u.save()

    user = User.objects.get(loginid_id=request.session['userid'])
    uid=user.id
    users = Cart.objects.filter(sid=uid,status2="pending",status1="buy")
    return render(request, 'seller/accept_order.html', {'users': users,'user':user})

def reject_order(request, id):
    u = Cart.objects.get(id=id)
    u.status2 = "rejected"
    u.save()

    user = User.objects.get(loginid_id=request.session['userid'])
    uid = user.id
    users = Cart.objects.filter(sid=uid, status2="pending",status1="buy")
    return render(request, 'seller/accept_order.html', {'users': users, 'user': user})

def order_details(request):
    user = User.objects.get(loginid_id=request.session['userid'])
    uid=user.id
    users = Cart.objects.raw('select * from customer_cart where sid_id=%s and status1="buy" and status2="accepted"order by sdate desc'% uid)
    total = 0
    for i in users:
        total = total + int(i.price)
    return render(request, 'seller/order_details.html', {'users': users,'user':user,'total':total})

def order_details_post(request):
    if request.method == 'POST':
        user = User.objects.get(loginid_id=request.session['userid'])
        uid=user.id
        mo = request.POST.get("month")
        ye = request.POST.get("year")
        users = Cart.objects.raw('select * from customer_cart where sid_id=%s and year(sdate)=%s and month(sdate)=%s and status1="buy" and status2="accepted"order by sdate desc',(uid,ye,mo))
        total = 0
        for i in users:
            total = total + int(i.price)
        return render(request, 'seller/order_details.html', {'users': users,'user':user,'total':total})

def customer_order_details(request,id):
    user = User.objects.get(loginid_id=request.session['userid'])
    p = Cart.objects.get(id=id)
    role = request.session["role"]
    return render(request, 'seller/customer_order_details.html', {'p': p,'user':user,'role':role})

def accept_rejected(request):
    user = User.objects.get(loginid_id=request.session['userid'])
    uid=user.id
    users = Cart.objects.filter(sid=uid,status2="rejected",status1="buy")
    return render(request, 'seller/accept_rejected.html', {'users': users,'user':user})

def accept_rejected_balance(request,id):
    u = Cart.objects.get(id=id)
    u.status2="accepted"
    u.save()

    user = User.objects.get(loginid_id=request.session['userid'])
    uid=user.id
    users = Cart.objects.filter(sid=uid,status2="rejected",status1="buy")
    return render(request, 'seller/accept_rejected.html', {'users': users,'user':user})

def delete_review(request,id1,id2):
    u = Review.objects.get(id=id1)
    u.delete()

    user = User.objects.get(loginid_id=request.session['userid'])
    pid = Product.objects.get(id=id2)
    reviews = Review.objects.filter(pid=pid)
    return render(request, 'seller/view_product.html', {'user': user,'p':pid,'reviews':reviews})