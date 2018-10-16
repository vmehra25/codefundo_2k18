from django.db import models

class user_details(models.Model):
    aadhar_no =models.TextField(max_length = 100,unique=True)
    pincode   =models.TextField(max_length = 50)
