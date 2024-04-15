from datetime import date

from django.shortcuts import render


# Create your views here.
from customer.models import Cart, Payment, Review
from login.models import User
from seller.models import Product

def gallery(request):
    user = User.objects.get(loginid_id=request.session['userid'])
    p = Product.objects.all()
    return render(request, 'customer/gallery.html', {'p': p,'user':user})

def about(request):
    user = User.objects.get(loginid_id=request.session['userid'])
    return render(request, 'customer/about.html', {'user':user})


def customer(request):
    role = request.session["role"]
    user = User.objects.get(loginid_id=request.session['userid'])
    p = Product.objects.all()
    return render(request, 'customer/customer.html',{'user':user,'p': p,'role':role})

def view_productc(request,id):
    user = User.objects.get(loginid_id=request.session['userid'])
    p = Product.objects.get(id=id)
    pro = Product.objects.all()
    d=p.cprice-p.sprice
    reviews=Review.objects.filter(pid=id)
    return render(request, 'customer/view_productc.html',{'pro':pro,'p':p,'d':d,'user':user,'reviews':reviews,'status':"Add to Cart"})

def product_dashc(request):
    user = User.objects.get(loginid_id=request.session['userid'])
    p = Product.objects.all()
    return render(request, 'customer/product_dashc.html', {'p': p,'user':user})

def cart(request,id):
    cid = User.objects.get(loginid_id=request.session['userid'])
    pid = Product.objects.get(id=id)
    s = pid.userid_id
    d = pid.cprice - pid.sprice
    sid = User.objects.get(id=s)
    reviews = Review.objects.filter(pid=id)
    s = Cart.objects.filter(sid=sid,pid=pid,cid=cid,status1='not').count()
    if(s==1):
        return render(request, 'customer/view_productc.html',{'user': cid, 'p': pid,'reviews':reviews, 'd': d, 'status': "Already Carted"})
    else:
        c = Cart()
        c.pid = pid
        c.cid = cid
        c.sid = sid
        c.price = pid.sprice
        c.save()
        return render(request, 'customer/view_productc.html',{'user': cid, 'p': pid,'reviews':reviews, 'd': d, 'status': "Carted Sucessfully"})

def view_cart(request):
    user = User.objects.get(loginid_id=request.session['userid'])
    uid=user.id
    p = Cart.objects.filter(cid=uid,status1='not')

    total=0
    for i in p:
        total=total+i.price
    gtotal=total+50
    return render(request, 'customer/view_cart.html', {'p': p,'user':user,'total':total,'gtotal':gtotal})

def delete_carted(request,id):
    user = User.objects.get(loginid_id=request.session['userid'])
    pr = Cart.objects.get(id=id)
    pr.delete()
    uid = user.id
    p = Cart.objects.filter(cid=uid,status1='not')

    total = 0
    for i in p:
        total = total + i.price
    gtotal = total + 50
    return render(request, 'customer/view_cart.html', {'p': p, 'user': user, 'total': total, 'gtotal': gtotal})

def update_qty(request,id):
    if request.method == 'POST':
        pro = Cart.objects.get(id=id)
        pro.qty = request.POST.get('qty')
        qty = int(request.POST.get('qty'))
        pro.price = qty*pro.pid.sprice
        pro.save()
        user = User.objects.get(loginid_id=request.session['userid'])
        uid = user.id
        p = Cart.objects.filter(cid=uid, status1='not')

        total = 0
        for i in p:
            total = total + i.price
        gtotal = total + 50
        return render(request, 'customer/view_cart.html', {'p': p, 'user': user, 'total': total, 'gtotal': gtotal})




def checkout_single_post(request,id):
    if request.method == 'POST':
        cid = User.objects.get(loginid_id=request.session['userid'])
        pid = Product.objects.get(id=id)
        s = pid.userid_id
        reviews = Review.objects.filter(pid=id)
        sid = User.objects.get(id=s)

        if pid.status == "not_available":

            return render(request, 'customer/view_productc.html',
                          {'user': cid, 'p': pid, 'status': "Carted Sucessfully",'reviews':reviews})

        c = Cart()
        c.pid = pid
        c.cid = cid
        c.sid = sid
        qty = int(request.POST.get('qty'))
        c.qty = qty
        price=pid.sprice
        c.price=price*qty
        total=c.price
        gtotal=total+50
        c.save()
        return render(request, 'customer/checkout_single.html', {'user': cid,'p':c,'total': total, 'gtotal': gtotal})

def checkout_single(request,id):
    cid = User.objects.get(loginid_id=request.session['userid'])
    p = Cart.objects.get(id=id)

    pid = Product.objects.get(id=p.pid_id)
    if pid.status=="not_available":
        return render(request, 'customer/view_productc.html', {'user': cid, 'p': pid,'status': "Carted Sucessfully"})

    total = p.price
    gtotal = total + 50
    p.save()
    return render(request, 'customer/checkout_single.html', {'user': cid, 'p': p, 'total': total, 'gtotal': gtotal})

def checkout_single_disp(request,id):
    cid = User.objects.get(loginid_id=request.session['userid'])
    p = Cart.objects.get(id=id)

    p.status1 = "buy"
    p.sdate = date.today()
    p.save()

    py = Payment()
    py.money = request.POST.get('gtotal')
    py.pcid = cid
    py.date= date.today()
    py.save()
    return render(request, 'customer/checkout_disp.html', {'user': cid, 'py': py})


def checkout_group(request):
    cid = User.objects.get(loginid_id=request.session['userid'])
    p = Cart.objects.filter( cid=cid, status1='not')

    total = 0
    for i in p:
        if i.pid.status == "available":
            total = total + int(i.price)
    gtotal = total + 50
    return render(request, 'customer/checkout_group.html', {'user': cid,'p':p, 'total': total, 'gtotal': gtotal})

def checkout_group_disp(request):
    cid = User.objects.get(loginid_id=request.session['userid'])
    p = Cart.objects.filter( cid=cid, status1='not')

    for i in p:
        if i.pid.status == "available":
            i.status1 = "buy"
            i.sdate = date.today()
            i.save()

    py = Payment()
    py.money = request.POST.get('gtotal')
    py.pcid = cid
    py.date= date.today()
    py.save()
    return render(request, 'customer/checkout_disp.html', {'user': cid,'py': py})




def pending_order(request):
    cid = User.objects.get(loginid_id=request.session['userid'])
    p = Cart.objects.filter(cid=cid, status1='buy',status2='pending')
    return render(request, 'customer/pending_order.html',{'user':cid,'p':p})

def order_history(request):
    cid = User.objects.get(loginid_id=request.session['userid'])
    p = Cart.objects.filter(cid=cid, status1='buy')
    return render(request, 'customer/order_history.html',{'user':cid,'p':p})

def add_review(request,id):
    if request.method == 'POST':
        cid = User.objects.get(loginid_id=request.session['userid'])
        pid = Cart.objects.get(id=id)
        pc=pid.pid
        r=Review()
        r.pid=pc
        r.cid=cid
        r.review=request.POST.get('review')
        r.save()

        p = Cart.objects.filter(cid=cid, status1='buy')
        return render(request, 'customer/order_history.html', {'user': cid, 'p': p})

    cid = User.objects.get(loginid_id=request.session['userid'])
    p = Cart.objects.get(id=id)

    if p.status2 == 'rejected':
        p = Cart.objects.filter(cid=cid, status1='buy')
        return render(request, 'customer/order_history.html', {'user': cid, 'p': p})

    return render(request, 'customer/add_review.html',{'user':cid,'p':p})


def cancel_order(request, id):
    cid = User.objects.get(loginid_id=request.session['userid'])
    pid = Cart.objects.get(id=id)
    if pid.status2=="pending":
        pid.delete()
        p = Cart.objects.filter(cid=cid, status1='buy',status2="pending")
        return render(request, 'customer/pending_order.html', {'user': cid, 'p': p})
    else:
        pid.delete()
        p = Cart.objects.filter(cid=cid, status1='buy')
        return render(request, 'customer/order_history.html', {'user': cid, 'p': p})
