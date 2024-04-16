from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    mail = models.EmailField()
    pincode = models.IntegerField()
    city = models.CharField(max_length=20,null=True)
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class register(models.Model):
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    smoking = models.BooleanField()
    hobbies = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    adharNumber = models.CharField(max_length=200)
    start = models.DateField(default="2021-01-01")
    end = models.DateField(default="2021-01-01")


class booking(models.Model):
    name = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    to = models.CharField(max_length=200)