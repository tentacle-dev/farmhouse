from datetime import datetime

from django.db import models

from login.models import User
from seller.models import Product


class Cart(models.Model):
    sid = models.ForeignKey(User,on_delete=models.CASCADE, related_name="sid")
    cid = models.ForeignKey(User, on_delete=models.CASCADE,related_name="cid")
    pid = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    status1 = models.CharField(max_length=20,default="not")#buy/not
    status2 = models.CharField(max_length=20,default="pending") #accepted/pending/rejected
    date = models.DateField(default=datetime.now)
    sdate = models.DateField(default=datetime.now)

class Payment(models.Model):
    pcid = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)

class Review(models.Model):
    cid = models.ForeignKey(User, on_delete=models.CASCADE)
    pid = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    date = models.DateField(default=datetime.now)

