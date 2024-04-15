from datetime import datetime

from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role=models.IntegerField()  # 0-admin 1-seller 2-customer
    date = models.DateField(default=datetime.now)

class User(models.Model):
    loginid = models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email=models.EmailField()
    phone = models.CharField(max_length=20)
    profilepic = models.ImageField(upload_to='images')
    role = models.IntegerField() # 0-admin 1-seller 2-customer
    status = models.CharField(max_length=10) # accept & not
    date = models.DateField(default=datetime.now)

class Feedback(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    feedback=models.TextField(max_length=500)
    role = models.IntegerField() # 0-admin 1-seller 2-customer
    date=models.DateField(default=datetime.now)

