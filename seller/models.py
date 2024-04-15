from django.db import models

from login.models import User


class Product(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    pname=models.CharField(max_length=50)
    bname=models.CharField(max_length=50,default="none")
    qty=models.CharField(max_length=10)
    pd=models.TextField(max_length=500)
    p_pic = models.ImageField(upload_to='images')
    cprice = models.IntegerField()
    sprice = models.IntegerField()
    status = models.CharField(max_length=20,default="available")
    rating=models.IntegerField(default=0)
