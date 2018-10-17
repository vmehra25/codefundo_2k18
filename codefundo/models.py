from django.db import models
from django.contrib.auth.models import User
class user_details(models.Model):
    aadhar_no =models.IntegerField(max_length = 100,unique=True)
    pincode   =models.IntegerField(max_length = 50)

class track_users(models.Model):
    pincode = models.IntegerField(max_length=100,unique=True)
    user_count=models.IntegerField(max_length=100000)