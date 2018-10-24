from django.db import models
from django.contrib.auth.models import User
class user_details(models.Model):
    aadhar_no =models.IntegerField(default=0,unique=True)
    pincode   =models.IntegerField(default = 50)
    city  = models.TextField(max_length=100,default="asdf")

class track_users(models.Model):
    pincode = models.IntegerField( unique=True)
    user_count=models.IntegerField(default=0)
    city  = models.TextField(max_length=10,default="asdf")


class gov_fund(models.Model):
    fund = models.IntegerField(default=0)

class people_review(models.Model):
    review= models.TextField(max_length=100)